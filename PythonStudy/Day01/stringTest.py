#1. 문자열 길이 구하기(함수)
a = "Life is too hard"
b = len(a)
print(b)

#2 인덱싱 : 가리킨다. 데이터의 위치값을 지목함.
#슬라이싱: 잘라낸다.

print(a[15])

# 문자열
d = "Life is short, You need Python"
f = d[0]+d[1]+d[2]+d[3]
k = d[0:4] # 0~3까지 잘라낸다. 4는 포함하지 않는다.
print(f)
print(k)
print(d[15:30]) # 15~29까지 잘라낸다. 30은 포함하지 않는다.

