#13 짝수만 필터링해서 새 리스트 만들기
numbers = [3, 8, 15, 22, 7, 40, 11, 6]
list_new = []
for ind in numbers:
    if ind % 2 == 0:
        list_new.append(ind)
print(list_new)

#리스트 컴프레션 방식을 이용해서 짧게 바꾸기
even_list1 = [n for n in numbers if n%2 ==0]
print(even_list1)