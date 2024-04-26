# CPU 바운드
# 프로그램이 실행될 때 실행 속도가 CPU 속도에 의해 제한됨을 의미
# 정말 복잡한 수학 수식을 계산하는 경우 컴퓨터 실행 속도가 느려지는 거
# CPU가 너무 많이 실행을 해서 프로그램 실행을 막는 경우
def cpu_bound_func(number: int):
    total = 1
    arrange = range(1, number + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k
    return total


if __name__ == "__main__":
    result = cpu_bound_func(10) # 100까지 늘리면 멈춤
    print(result)