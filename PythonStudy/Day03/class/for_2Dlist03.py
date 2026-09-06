for i in range(10):
    print(i)
print()
#거꾸로 뽑고 싶을때
for i in range(10,-1,-1):
    print(i)
print()
# reversed() 함수
numbers = [10, 20, 30, 40, 50]
# numbers는 장부 10,20,30...에 대한 데이터에 접근하기 위한 주소 값이다.
# 첫 주소값을 알고 있으면 이후의 데이터를 참조 해서 접근 할 수 있다.
# EX)인스타에서 타고타고 들어가는것.
for number in numbers:
    print(number)
print()
for number in reversed(numbers):
    print(number)
print()
for number in numbers[::-1] :
    print(number)
print()
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]