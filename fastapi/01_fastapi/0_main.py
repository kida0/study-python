from fastapi import FastAPI, Query
from typing import List, Dict, Optional, Union


app = FastAPI()

@app.get("/")
def main():
    return {"message": "hello"}

@app.get("/hello")
def hello():
    return {"hello": ":)"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return{"item_id": item_id}

@app.get("/users/{user_id}/items/{item_name}")
def read_user_item(user_id: int = 11, item_name: str = "somsatang"):
    return {"user_id": user_id, "item_name": item_name}

#127.0.0.1:8000/items/?skip=3&limit=5
@app.get("/items/")
def read_items(skip = 0, limit = 10):
    return {"skip": skip, "limit": limit}

@app.get("/list/")
async def read_list(q: List[int] = Query([])):
# async def read_list(q: List[int] = Query([1, 2])):    # default 값 지정
    return {"q": q}

@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item

@app.get("/dataitems/")
async def read_itmes(data: Optional[int] = None):   # None을 반드시 지정해줘야 함
    return data

# @app.get("/dataitems/")
# async def read_itmes(data: Union[int, str]):   # int 또는 str을 받는 형태
#     return data

@app.get("/hm/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.post("/hm/")
def create_item(item: dict):
    return {"item": item}

@app.put("/hm/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}

@app.delete("/hm/{item_id}")
def delete_item(item_id: int):
    return {"message": f"item {item_id} has been deleted"}


