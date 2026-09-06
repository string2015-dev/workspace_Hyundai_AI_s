#문자열 내 특정 문자 개수 세기
sentence = "banana"
target = "a"
lenth = []
for i in range(len(sentence)):
    if target == sentence[i]:
        lenth.append(sentence[i])
print(len(lenth))