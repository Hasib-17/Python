from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
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

Selection=dict[
    str,str|int|float|Category|None
]

@app.get("/")
def index() ->dict[str, dict[int,Iteam]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_by_item_id(item_id:int)->Iteam:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"Iteam with {item_id} does not exist."
        )
    return items[item_id]


@app.get("/items")
def query_item_by_parameters(
    name: str|None=None,
    price: float| None=None,
    count: int| None=None,
    category: Category|None=None,

) -> dict[str, Any]:
    def check_item(item: Iteam) ->bool:
        return all(
            (
                name is None or item.name==name,
                price is None or item.price==price,
                count is None or item.count==count,
                category is None or item.category is category,
            )
        )
    Selection=[item for item in items.values() if check_item(item)]
    return{
        "query": {
            "name": name, 
            "price": price, 
            "count": count, 
            "category": category, "selection": Selection,
        }
    }

  
    