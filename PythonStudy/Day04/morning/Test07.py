#7 리스트에서 짝수 세기
numbers = [3, 8, 15, 22, 7, 40, 11]
list = []
for i in numbers:
    if i % 2 == 0 :
        list.append(i)
print(f"{len(list)} 개")


#comprehension generation 파이썬 다운 형태다.
count = sum(1 for number in numbers if number %2 == 0)
print(count)

