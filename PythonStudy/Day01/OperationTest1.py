number = 100
number += 10
print(number)
number -= 10
print(type(number))
number *= 10
print(number)
number /= 10 #나누기는 float형으로 나온다.
print(type(number))
number %= 10
print(number)
print(type(number))

a = 101
# 짝수인지 홀수인지 판별하는 프로그램
if a%2 == 0 :
    print("짝수")
else:
    print("홀수")
