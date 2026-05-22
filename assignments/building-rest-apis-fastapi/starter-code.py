from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items: list[dict[str, Any]] = [
    {"id": 1, "name": "Sample Item", "description": "This is a starter record."},
]


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items")
def get_items() -> list[dict[str, Any]]:
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict[str, Any]:
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item) -> dict[str, Any]:
    new_id = max((record["id"] for record in items), default=0) + 1
    new_item = {"id": new_id, **item.model_dump()}
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict[str, Any]:
    for index, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            updated_item = {"id": item_id, **item.model_dump()}
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    for index, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            items.pop(index)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
