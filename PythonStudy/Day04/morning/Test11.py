#11 구구단 2~9단 전체 출력하기.(중첩 for)

for x in range(2,10):
    for y in range(1,10):
        print(x*y)
print()
#while 문을 이용해서 구구단 만들기.
n = 2
# while는 시작전 기준점이 반드시 필요하다.
while n <= 9:
    i = 1
    while i <= 9:
        print(f"{n} X {i} = {n*i}")
        i += 1
    n += 1