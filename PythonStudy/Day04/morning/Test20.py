#20 while + break 누적합이 목표값을 넘는 순간 찾기
sum = 0
n = 1
while sum <= 500:
    sum += n
    n += 1
print(n-1)
print()

#다시 짜본 코드
fals =-1
n = 1
while True:
    if (n*(n+1))/2 <= 500:
        print(fals)
        n+=1
    elif (n*(n+1))/2 >500:
        print(n)
        break
