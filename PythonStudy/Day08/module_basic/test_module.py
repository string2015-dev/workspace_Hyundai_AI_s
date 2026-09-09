# test_module.py 파일
PI = 3.141592 # 상수가 들어가 있음

def number_input(): # 함수가 정의
    output = input("숫자 입력> ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius
#각각의 함수의 기능이 공통점이 있음. 여기서는 원에관련!
# => 즉 구조화가 필요하다.