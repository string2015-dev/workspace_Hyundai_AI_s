# 정수 3개를 입력 받아 그중 가장 큰 수를 출력하는 프로그램을 작성하시오. 
# 출력 조건)  입력을 받기 전 "세 수를 입력하세요. "을 출력한다.
# 입력을 받은 후 "입력받은 수 중 가장 큰 수는 {가장 큰 수}입니다."를 출력한다.

#정수를 3번 입력할 수 있게 input()함수 3개를 사용한다.
n1 = int(input("첫번쨰 정수를 입력하세요: "))
n2 = int(input("두번째 정수를 입력하세요: "))
n3 = int(input("세번쨰 정수를 입력하세요: "))
#가장큰 수를 찾기 위해 max()함수를 이용한다.
big = max(n1, n2, n3)
#가장 큰 수를 출력한다.
print("입력받은 수 중 가장 큰 수는 {}입니다.".format(big))

#출력 조건을 입력 받기전 "세 수를 입력하세요." 를 출력한다.
print("세 수를 입력하세요")
n1 = int(input())
n2 = int(input())
n3 = int(input())
#입력받은 수중 가장 큰 수 찾기
if n1 > n2 and n1 > n3 :
    print(f"{n1}가장 큰 수 입니다.")
elif n2 > n1 and n2 > n3 :
    print(f"{n2}가장 큰 수 입니다.")
elif n3 > n1 and n3 > n2 :
    print(f"{n3}가장 큰 수 입니다.")
#{가장 큰 수} 입니다.

#강사님 코드
print("세 수를 입력하세요")
n1 = int(input())
n2 = int(input())
n3 = int(input())
#입력받은 수중 가장 큰 수 찾기
if n1 > n2 and n1 > n3 :
    biggest = n1
elif n2 > n1 and n2 > n3 :
    biggest = n2
elif n3 > n1 and n3 > n2 :
    biggest = n3

print({}.format(biggest))
print("{}입니다.".format(biggest))
print(f"{bigggest}입니다.")