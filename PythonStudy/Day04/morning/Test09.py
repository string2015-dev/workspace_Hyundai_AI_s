#9 리스트에서 특정 값의 인덱스 찾기(break활용) 57이 몇 번째 인덱스에 있는지 확인하시오
array = [273, 32, 103, 57, 52]
for i in array:
    if i == 57:
        print(array.index(i))
print()
# 선형탐색방법

#method-1 : range()
t_num = 57
idx = -1
for i in range(len(array)):
    if array[i] == t_num:
        idx =i
        break
print(idx)
print()

#method-2 에뮬레이터.
for i, v in enumerate(array):
    if v == t_num:
        print(i)
        break
    else: print(-1)