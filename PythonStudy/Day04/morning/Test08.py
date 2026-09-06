#8 문자열 거꾸로 출력하기
word = "Python"
rev = []
for i in reversed(word):
    rev.append(i)
print(rev)


#
word = "python"
for ch in reversed(word):
    print(ch, end="")
print()
#join이용
result = ''.join(reversed(word))
print(result)
