#21 리스트 뒤집기
# reverse()나 슬라이싱 없이 반복문으로 리스트를 뒤집어보세요.
numbers = [1, 2, 3, 4, 5]
rever_num = []
for i in range(-1,-6,-1):
    rever_num.append(numbers[i])
print(rever_num)