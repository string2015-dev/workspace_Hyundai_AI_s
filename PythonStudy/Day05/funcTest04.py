# 리스트에서 특정 값의 위치와 개수 찾기
fruits = ["apple", "banana", "apple", "cherry", "apple"]
target = "apple"

a_idx = fruits.index(target)

print(f"{a_idx}은 {target}이 처음 등장하는 인덱스입니다.")

count = [word for word in fruits if word == target]

print(f"{len(count)}은 {target}이 반복된 횟수 입니다.")

# 강사님 풀이.
# 에플이 언제 처음 등장 하는지와 몇 번 반복되는지 두가지를 확인해야한다.
# .index를 이용해서 언제 처음

#컴프리헨션 (제너레이터) 으로 리 팩토링
le_idx = next(i for i, v in enumerate(fruits) if v == "apple")
