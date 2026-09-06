#22 소수 판별하기
numbers =25
검증 = []
n = 1
while True:
    if numbers % n == 0 and n <= numbers:
        검증.append(n)
        n+=1
    elif numbers % n != 0 and n <= numbers:
        n+=1
    else:
        if len(검증) == 2 :
            print("number는 소수다.")
            break
        else:
            print("error 소수가 아닙니다.")
            break