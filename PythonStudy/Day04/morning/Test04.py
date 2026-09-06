#4 리스트에서 최댓값 찾기(내장 함수 없이)
# 반복문으로 최댓값을 찾아보세요.
list = [10, 4, 7, 9, 13, 51, 42, 74, 29, 11]
a = sorted(list)
print(a[-1])
print()
#
max_value = [list[0]]
for i in range(len(list)):
    if max_value[0] < list[i] :
        max_value.pop()
        max_value.append(list[i])
print(max_value[0])
