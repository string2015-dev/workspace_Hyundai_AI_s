# 18 리스트 최댓값/최솟값 동시에 찾기

numbers = [45, 12, 89, 3, 67, 21]
max = 0
min = numbers[0]
for i in numbers:
    if max < i :
        max = i
for j in numbers:
    if min > j:
        min = j
            
print(f"{max}최댓값 {min}최솟값")