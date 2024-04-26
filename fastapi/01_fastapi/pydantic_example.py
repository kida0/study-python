from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()


class ItemA(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    is_offer: bool = None


class Item(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, title="Item Name")
    price: float = Field(..., get=0, description="The price must be greater than zero")
    description: str = Field(None, description="The description of the item")
    tag: List[str] = Field(default=[], alias="item-tag")
    # 내외부 처리 필드를 다르게 가져가 때 alias 사용

    
@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()}

# nested model
class Image(BaseModel):
    url: str
    name: str
    
class Item(BaseModel):
    name: str
    description: str
    image: Image