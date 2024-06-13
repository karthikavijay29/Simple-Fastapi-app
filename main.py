from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items: List[Item] = []

@app.get("/items")
async def get_items() -> List[Item]:
    """Retrieve all items. Returns a list of all items."""
    return items

@app.post("/items")
async def create_item(item: Item) -> Item:
    """Create a new item. Returns the created item."""
    items.append(item)
    return item

@app.get("/items/{item_id}")
async def get_item(item_id: int) -> Union[Item,None]:
    """Retrieve an item by its ID. Returns the item if found, otherwise raises an HTTPException."""
    for item in items:
        if item.id == item_id:
            return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item) -> Union[Item,None]:
    """Update an existing item by its ID. Returns the updated item if found, otherwise raises an HTTPException."""
    for idx, item in enumerate(items):
        if item.id == item_id:
            items[idx] = updated_item
            return updated_item

@app.patch("/items/{item_id}")
async def patch_item(item_id: int, updated_item: Item) -> Union[Item,None]:
    """Partially update an existing item by its ID. Returns the updated item if found, otherwise raises an HTTPException."""
    for idx, stored_item in enumerate(items):
        if stored_item.id == item_id:
            update_data = updated_item.dict(exclude_unset=True)
            updated_item = stored_item.copy(update=update_data)
            items[idx] = updated_item
            return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int) -> Union[Item,None]:
    """Delete an item by its ID. Returns the deleted item if found, otherwise raises an HTTPException."""
    for idx, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(idx)
            return deleted_item
