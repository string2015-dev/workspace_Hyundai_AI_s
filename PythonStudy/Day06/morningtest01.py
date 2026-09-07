# 문제: 학생 5명의 점수가 담긴 리스트 scores = [85, 92, 78, 90, 88]이 있습니다. 
# for문을 사용해 총합과 평균을 구해 출력하세요.
scores = [85, 92, 78, 90, 88]
sum = 0
for i in scores:
    sum += i
average = sum/len(scores)
print(f"총합{sum}, 평균{average}")