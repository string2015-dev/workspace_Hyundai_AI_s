#15 리스트 중복 제거하기 (반복문)
numbers = [1, 3, 2, 3, 5, 1, 4, 2]

#빈 리스트를 만든다.
#넘버의 리스트를 처음부터 끝까지 한번 루프 해서 한 번 한번만 등장한 수를 제거한다.
#지워진 값을 새로운 리스트에 담아둔다.

# 다시.

#키와 값...?ㅋㅋㅋㅋ

#각 수와 겹침수.
count = {}

for i in numbers:
    if count.get(i) == None:    # "None"이 아닌 None 사용
        count[i] = 1            # 처음 발견된 숫자는 개수 1 저장
    else:
        count[i] += 1           # 이미 존재하면 개수 1 증가

print(count) 
for i in count:                 # "키" 를 i변수에 담는다.
    for j in range(count[i]-1): # 중복갯수 -1만큼 반복한다.
        numbers.remove(i)       # "키" 값을 찾아서 제거한다.
print(numbers)                  # 중복된 숫자를 제거한 리스트를 출력