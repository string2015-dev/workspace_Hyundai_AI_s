list_a = [1,2,3,4,5]
#map 함수에 람다 사용.
output_a = map(lambda x: x*x,list_a)

output_b = filter(lambda x: x<3,list_a)

print("output_a:",list(output_a))

print("output_b:",list(output_b))