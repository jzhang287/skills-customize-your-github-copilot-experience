from typing import Any

import sqlite3
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

DB_PATH = "data.sqlite3"

app = FastAPI()


class NoteCreate(BaseModel):
    title: str
    content: str


class Note(NoteCreate):
    id: int


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/notes")
def list_notes(q: str | None = None) -> list[dict[str, Any]]:
    conn = get_db_connection()
    if q:
        cur = conn.execute("SELECT * FROM notes WHERE lower(title) LIKE ?", (f"%{q.lower()}%",))
    else:
        cur = conn.execute("SELECT * FROM notes")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/notes/{note_id}")
def get_note(note_id: int) -> dict[str, Any]:
    conn = get_db_connection()
    cur = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Note not found")
    return dict(row)


@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate) -> dict[str, Any]:
    conn = get_db_connection()
    cur = conn.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (note.title, note.content))
    conn.commit()
    note_id = cur.lastrowid
    conn.close()
    return {"id": note_id, "title": note.title, "content": note.content}


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate) -> dict[str, Any]:
    conn = get_db_connection()
    cur = conn.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Note not found")
    conn.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (note.title, note.content, note_id))
    conn.commit()
    conn.close()
    return {"id": note_id, "title": note.title, "content": note.content}


@app.delete("/notes/{note_id}")
def delete_note(note_id: int) -> dict[str, str]:
    conn = get_db_connection()
    cur = conn.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    if not cur.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Note not found")
    conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return {"message": "Note deleted"}


if __name__ == "__main__":
    print("Run with: uvicorn starter-code:app --reload")
