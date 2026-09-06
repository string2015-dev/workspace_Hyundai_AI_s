#5 딕셔너리에서 값 꺼내고 키 목록 확인하기
info = {"name": "김민수", "age": 25, "job": "학생"}

age = info.get("age")

allkey = info.keys()

print(f"{age}는 나이 입니다.{allkey}는 info의 모든 key입니다.")

#강사님 코드
keyset = info.keys()
for key in keyset:
    print(key)
print(info.keys())
print(list(info.keys()))