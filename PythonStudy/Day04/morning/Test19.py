#19 딕셔너리에서 조건을 만족하는 키만 추출하기
scores = {"철수": 85, "영희": 72, "민수": 91, "지은": 68}
name = []
for i in scores:
    if 80 <= scores[i]:
        name.append(i)
print(name)