# 📘 Assignment: Intro to API Persistence with SQLite

## 🎯 Objective

Build a simple CRUD REST API with FastAPI that persists data to a local SQLite database. Students will learn how to model data, perform basic SQL operations, and connect an API to persistent storage.

## 📝 Tasks

### 🛠️	Create a CRUD API backed by SQLite

#### Description
Implement a FastAPI application that supports creating, reading, updating, and deleting simple `notes` stored in a SQLite database file.

#### Requirements
Completed program should:

- Expose the following endpoints:
  - `GET /notes` — return all notes
  - `GET /notes/{id}` — return a single note by id
  - `POST /notes` — create a new note
  - `PUT /notes/{id}` — update an existing note
  - `DELETE /notes/{id}` — delete a note
- Persist data to a SQLite database file (create the table automatically if missing).
- Use Pydantic models for request validation and response shapes.
- Return appropriate HTTP status codes (e.g., 201 for create, 404 when not found).

Example `POST /notes` request body:

```json
{
  "title": "Shopping list",
  "content": "Eggs, milk, bread"
}
```

Example `GET /notes` response:

```json
[
  {"id": 1, "title": "Shopping list", "content": "Eggs, milk, bread"}
]
```

### 🛠️	(Stretch) Add simple search

#### Description
Add a query parameter to `GET /notes` to filter notes by title substring.

#### Requirements

- Accept `?q=<term>` on `GET /notes` and return notes with `title` containing `<term>` (case-insensitive).
