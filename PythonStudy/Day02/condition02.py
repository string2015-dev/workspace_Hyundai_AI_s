number = int(input("정수 입력 > "))

last_number = number % 10

if last_number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")


# 다른 방법 
number = input("정수 입력> ")
last_character = number[-1]

# 짝수 조건
if last_character in "02468":    print("짝수입니다")

# 홀수 조건
if last_character in "13579":    print("홀수입니다")