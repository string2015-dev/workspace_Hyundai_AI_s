tuple_test = 10, 20, 30, 40
print("괄호없는 튜플의 값과 자료형 출력: ")
print("tuple_test: ",tuple_test)
print(type(tuple_test))

#괄호가 없는 튜플 테스트 tuple_test01에 자신의 이름과 친구 2명의 이름을 할당후 출력

tuple_test01 = "정현", "친구1", "친구2"
print("친구들: ",tuple_test01)
# 본인 이름과 친구들 이름을 인덱스 이용해서 출력
print(tuple_test01[0], tuple_test01[1], tuple_test01[2])
#for 출력
for i in range(len(tuple_test01)):
    frd = tuple_test01[i]
    print(frd)

for name in tuple_test01:
    print(f"이름 : {name}")