list_a = [273, 32, 103, "문자열", True, False]
print(list_a[3])
print(list_a[3][0])
print(list_a[3][1])
print(list_a[3][2]) # 반복문을 이용해 한줄로 처리 하게 할 수 도 있다.

list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_1 = list_a[0][2]
print(list_1)
# list_1 변수의 3과 
list_2 = list_a[2][1]
print('{} + {} = {}'.format(list_1, list_2, list_1 + list_2))

list = [["PHK"],["OYJ"],["TNQ"]]
p = list[0][0]
y = list[1][1]
t = list[2][0]
h = list[0][1]
o = list[1][0]
n = list[2][1]
print("{}{}{}{}{}{}{}".format(p, y, t, h, o, n))
