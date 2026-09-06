#1 리스트 합계 구하기
numbers = [12, 25, 7, 33, 18]
sum1 = 0
for sum in numbers:
    sum1 += sum
print(sum1)

sum1 = sum1 + numbers[0]

sum1 = sum1 + numbers[1]