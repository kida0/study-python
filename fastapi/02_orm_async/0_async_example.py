import asyncio


async def func1():
    print("func1: Start")
    await asyncio.sleep(2)
    print("func1: End")
    
async def func2():
    print("func2: Start")
    await asyncio.sleep(1)
    print("func2: End")
    
async def main():
    await asyncio.gather(func1(), func2())
    
if __name__ == "__main__":
    asyncio.run(main())
    
    
###


from fastapi import FastAPI
import asyncio

app = FastAPI()

# fastapi가 비동기 처리를 지원하더라도, 내부 함수가 비동기 처리되도록 구현되어 있어야 함
# 라이브러리가 비동기 처리를 해줘야 함
# CPU 작업은 비동기의 이점을 많이 누리지 못하지만, IO의 경우 비동기 처리가 유의미
async def fetch_data():
    await asyncio.sleep(3)
    return {"data": "some_data"}

@app.get("/")
async def read_root():
    data = await fetch_data()
    return {"message": "Hello, world!", "fetched_data": data}