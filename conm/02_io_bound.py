# 프로그램이 실행될 때 실행 속도가 I/O에 의해 제한됨을 의미
# I: input, O: output
# 사용자가 입력을 하지 않으면 멈춘 것처럼, 컴퓨터와 컴퓨터끼리 통신을 할 때에도 I/O 바운드 발생
# 구글 홈페이지를 입력하면 약 2초 후에 페이지가 뜨는데, 이 2초는 네트워크 I/O 바운드 때문에 생김!
# 블로킹: 바운드에 의해 코드가 멈추게 되는 현상
import requests

def io_bound_func():
    print("값을 입력해주세요")
    input_value = input()
    return int(input_value) + 100


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for i in range(10):
        result = io_bound_func()    # 바운드에 의해 코드가 총 10번 멈췄기 때문에, 10번 블로킹 당한 것
    print(result)
    