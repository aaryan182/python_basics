from fastapi import FastAPI, HTTPException
from prisma import Prisma
from pydantic import BaseModel

app = FastAPI()
prisma = Prisma()
prisma.connect()

class ItemCreate(BaseModel):
    name: str
    description: str | None = None

@app.post("/items/")
async def create_item(item: ItemCreate):
    new_item = await prisma.item.create(data=item.dict())
    return new_item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = await prisma.item.find_unique(where={"id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/")
async def read_items():
    return await prisma.item.find_many()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemCreate):
    updated_item = await prisma.item.update(
        where={"id": item_id},
        data=item.dict()
    )
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    await prisma.item.delete(where={"id": item_id})
    return {"message": "Item deleted"}


                                                                     