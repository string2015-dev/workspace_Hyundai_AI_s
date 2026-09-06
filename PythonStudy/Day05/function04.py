# 확인문제1다음과 같이 방정식을 파이썬 함수로 만들어 보세요.

#  f(x) = 2x + 1

# 확인문제2 다음 빈칸을 채워 매개변수로 전달된 값들을 모두 곱해서 
# 리턴하는 가변 매개변수 함수를 만들어 보세요.
def mul(*values):  
    output = 1
    for i in values:
        output *= i
    return output


# 함수를 호출합니다.
print(mul(5, 7, 9, 10))

student = {"name": "클라라", "course": "AI서비스개발"}
print(student["name"])          # 출력: 클라라
print(student.get("age"))       # 출력: None (에러 없이 안전하게 처리, "age" 서랍이 없음)
print(student.get("age","name"))   # 출력: 20 (없을 때 기본값 지정 가능)