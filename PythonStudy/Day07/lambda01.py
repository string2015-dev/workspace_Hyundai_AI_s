# 함수를 선언
power = lambda x: x*x
under_3 = lambda x: x<3
list_a = [1,2,3,4,5]
#map 함수에 람다 사용.
output_a = map(power,list_a)

output_b = filter(under_3,list_a)

print("output_a:",list(output_a))

print("output_b:",list(output_b))