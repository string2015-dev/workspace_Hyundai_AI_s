# - **문제**: `while`문을 사용해 사용자가 입력한 숫자(2~9)의 구구단을 출력하세요.
# - **출력 예시**: `3 x 1 = 3`, `3 x 2 = 6` ... `3 x 9 = 27`
num = int(input())
count = 0
while count < 10:
    for i in range(1,10):
        mult = num *i
        print(f"{num} X {i} = {mult}", end = ",")
        count+=1