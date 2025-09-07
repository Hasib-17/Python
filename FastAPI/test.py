from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Category(Enum):
    TOOLS="tools"
    CONSUMABLE="consumable"

class Iteam(BaseModel):
    name:str
    price:float
    count:int
    id:int
    category:Category

items={
    0:Iteam(name="Hammer",price=9.99,count=20,id=0,category=Category.TOOLS),
    1:Iteam(name="Pliers",price=5.99,count=15,id=1,category=Category.TOOLS),
    2:Iteam(name="Nails",price=13.99,count=35,id=2,category=Category.TOOLS),
}

@app.get("/")
def index() ->dict[str, dict[int,Iteam]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_by_item_id(item_id:int)->Iteam:
    if item_id not in items:
        raise HTTPException(
            status_code=404, details=f"Iteam with {item_id} does not exist."
        )
    return items[item_id]


