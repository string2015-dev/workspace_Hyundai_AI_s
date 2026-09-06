data = [1, 2, 3, 4,]
data1 = ["안", "녕", "하", "세", "요"]
data2 = [273, 32, 103, "문자열", True, False]

#변수 data 첫번째 요소의 값을 list1 이라는 변수에 저장하세요.
list1 = data[0]
#list1에 저장된 값을 출력하고 숫자라면 해당 값에 2를 더하시오
print(list1)
list1 = list1 + 2
print(list1)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data 리스트의 3번째 요소와 5번째 요소의 값을 합하여 list2라는 변수에 저장 후 출력하세요.
list2 = data[2] + data[4] # int로 숫자 타입을 줄 필요가 없다 리스트에 숫자형으로 저장되어 있어서.
print(list2)
print('{} + {} = {}'.format(data[2], data[4], list2))

list3 = data[1:3]
print(list3)
print(data[1], data[2])
print(data[-3])

list_a = [273, 32, 103, "문자열", True, False]
print(list_a[3])
print(list_a[3][0])
