# 숫자 두 개를 매개변수로 받아 덧셈, 뺄셈, 곱셈, 나눗셈 
# 결과를 각각 반환하는 함수 4개
# (add, subtract, multiply, divide)를 정의하고 호출해보세요.

def add(x,y) :
    return int(x) + int(y)

def subtract(x,y) :
    return int(x) - int(y)

def multiply(x,y) :
    return int(x)*int(y)
def divide(x,y):
    if y == 0:
        return ("0으로 나눌 수 없습니다.")
    else: return f"{int(x)/int(y):.2f}"

print(add(234,3452))
print("뺄셈",subtract(3452,-3948572))
print("곱셈", multiply(2345,2349857))
print("나눗셈",divide(23452,9865) )