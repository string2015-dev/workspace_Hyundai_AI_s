#2 리스트 평균 구하기
# 문제 1의 로직을 응횽해 평균을 구해보세요.
numbers = [12, 25, 7, 33, 18]
sum1 = 0
for sum in numbers:
    sum1 += sum
print(sum1/int(len(numbers)))