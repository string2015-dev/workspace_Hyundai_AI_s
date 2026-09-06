#24 버블정렬로 리스트 오름차순 정렬하기
numbers = [5, 2, 9, 1, 7]

i = 0
while i < 4:
    
    if numbers[i] > numbers[i+1]:
        numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
        i = 0
    else: i +=1
print(numbers)
#인접한 두 수를 바꾸면서 나아가는 건데
#안 바뀌면 처음부터 봐야한다고 생각했음
# 그때 진행되지 않아서 조건을
    
