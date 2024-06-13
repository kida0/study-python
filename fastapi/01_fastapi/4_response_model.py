from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    
    
def get_item_from_db(id):
    return {
        "name": "simple item",
        "description": "a simple description",
        "price": 5.0,
        "dis_price": 45.0,  # response_model인 Item에 들어가 있지 않기 때문에 출력X
    }
    
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item_from_db(item_id)
    return item


class Cat(BaseModel):
    name: str
    
class Dog(BaseModel):
    name: str
    
@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    if animal == "cat":
        return Cat(name="Whiskers")
    else:
        return Dog(name="Happy")
    

class Item(BaseModel):
    name: str
    
@app.get("/items/", response_model=List[Item])
async def get_items():
    return [{"name": "Item 1"}, {"name": "Iiem 2"}]
