# await를 기점으로 다른 코루틴으로 넘어가게 됨
# await는 단순히 비동기를 동기로 기다리는 역할이 아니라 함수를 처리할 때 사용하는 키워드
import time
import asyncio


async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")
    

async def main():
    await asyncio.gather(
        delivery("A", 3),
        delivery("B", 3),
        delivery("C", 4),
    )

# 이 코드는 동기로 작동    
# async def main():
#     await delivery("A", 3)
#     await delivery("B", 3)
#     await delivery("C", 4)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)