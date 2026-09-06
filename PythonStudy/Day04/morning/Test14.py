#14 두 리스트로 딕셔너리 만들기 (range 활용)
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

#각각의 인덱스[] == 인덱스[] 일떄 출력을 하게 하면 되지 않을까?
g = {}
for i in range(len(key_list)):
    for j in range(len(value_list)):
            if i == j:
                g[key_list[i]] = value_list[j]
print(g)

# 강사님 코드
print()
#구조를 먼저 만든다.
result = {}

for i in range(len(key_list)) :
     result[key_list[i]] = value_list[i]
print(result)

# zip() 함수 이용.
result1 = dict(zip(key_list,value_list))
print(result1)