# 파이썬 코루틴 -> 루틴: 일련의 명령(코드의 흐름)
# 메인 루틴: 프로그램의 메인 코드 흐름 -> if __name__ == "__main__": 이후 코드 흐름
# 서브 루틴: 함수나 메서드와 같이 하나의 진입점과 하나의 탈출점만 존재
# -> main()과 같은 1개의 진입점, 1개의 탈출점이 있는 함수 (참고) 'return'도 없는 함수 = 'return'만 있는 함수 = 'return None'
# 코루틴: 서브 루틴의 일반화된 형태로 다양한 진입점과 다양한 탈출점있는 루틴
# 파이썬 비동기 함수는 코루틴 함수로 만들 수 있음
import asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")                         # 진입점 1
    await asyncio.sleep(mealtime)                         # 진입점 2, 탈출점1 - 함수는 일시 중단되고 제어권을 이벤트 루프에 양도
    print(f"{name} 식사 완료, {mealtime} 시간 소요...")
    print(f"{name} 그릇 수거 완료")                         # 탈출점 2


#####
# 일반적인 서브루틴
def hello_world():
    print("hello world")
    return 123

# 동시성
async def main():
    result = await asyncio.gather(
        delivery("A", 1),
        delivery("B", 2),
        delivery("C", 3),
    )
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(hello_world()