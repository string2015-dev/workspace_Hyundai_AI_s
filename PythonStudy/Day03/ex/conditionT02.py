#정수 2개를 입력받아서 큰 수와 작은 수를 차례로 출력하는 프로그램을 작성하시오.
a = int(input("정수를 입력하세요: "))
b = int(input("정수를 입력하세요: "))
if a < b :
    print(f"입력받은 수 중 큰 수는 {b}이고 작은 수는 {a}입니다.")
elif a > b:
    print("입력받은 수 중 큰 수는 {}이고 작은 수는 {}입니다.".format(a, b))
else:
    print("입력받은 수 {}와(과) {}는 같습니다.".format(a, b))

# min과 max 활용
small = min(a,b)
big = max(a,b)
if a != b:
    print("입력받은 수 중 큰 수는 {}이고 작은 수는 {}입니다.".format(max(a, b),min(a, b)))
else:
    print("입력받은 수 {}와(과) {}는 같습니다.".format(a, b))

#1. 정수 2개를 입력받아야 한다.
#input()함수 두개와 변수 두개가 필요하다
num1 = int(input("첫번째 정수입력: "))
num2 = int(input("두번쨰 정수입력: "))
#2. 큰 수와 작은 수를 차례로 출력하는 프로그램
if num1 > num2:
    print("큰수", num1)
    print("작은수", num2)
else:
    print("큰수", num2)
    print("작은수", num1)