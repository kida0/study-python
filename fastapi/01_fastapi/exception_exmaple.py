from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/item/{item_id}")
def read_item(item_id: int):
    if item_id == 42:
        raise HTTPException(status_code=404, detail="Item not found")
    try: 
        if item_id < 0:
            raise ValueError("음수는 허용되지 않습니다")
    except ValueError as e:
        raise HTTPException(status_doe=400, detail=str(e))
            
    return {"item_id": item_id}