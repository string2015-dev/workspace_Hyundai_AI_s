#함수를 선언한다.
def power(item):
    return item*item

def under_3(item):
    return item <3

list_input_a = [1,2,3,4,5]

#map()함수 넣고 처리.
output_a = map(power, list_input_a)
print(output_a)
# => <map object at 0x0000026B91B49C00> map object가 생성이됐다는 뜻.
print(list(output_a))

# filter() 함수
output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))
#==============================================================
# 신기하게도 필터링을 이용해서 map 하면 True False를 나눠서 출력할 수 있다!
output_a = map(under_3, list_input_a)
print(output_a)
print(list(output_a))