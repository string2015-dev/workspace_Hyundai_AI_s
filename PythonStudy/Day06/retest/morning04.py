#### 4. 사칙연산 함수 만들기 — `[함수]`
# - **문제**: 숫자 두 개를 매개변수로 받아 덧셈, 뺄셈, 곱셈, 나눗셈 
# 결과를 각각 반환하는 함수 4개(`add`, `subtract`, `multiply`, `divide`)를 정의하고 호출해보세요.
# - 💡 **비유**: 함수는 "자판기"입니다. 재료(매개변수)를 넣으면 정해진 결과물(반환값)이 나오는 기계라고 생각하면 쉬습니다.
# - ⚠️ 나눗셈 함수는 0으로 나누는 경우도 고려해보세요
#======================================================================
def add(x,y) :
    return int(x) + int(y)

def subtract(x,y) :
    return int(x) - int(y)

def multiply(x,y) :
    return int(x)*int(y)
def divide(x,y):
    if y == 0:
        return ("0으로 나눌 수 없습니다.")
    else: return f"{int(x)/int(y)}"