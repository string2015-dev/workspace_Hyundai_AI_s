# 문장에서 단어 개수와 가장 긴 단어 찾기
sentence = "Python is a powerful and easy programming language"
#강사님 강의

#내가 세운 논리.
# 단어 개수와 긴 단어를 찾기 위해 .split으로 단어 단위로 잘라 새로운 리스트에 담는다.
# len() 함수르 이용해 리스트의 인덱스 갯수를 출력한다.
# 자른 단어를 len()함수로 -> 길이에 대한 숫자로 바꾼다.
# 숫자들 중 가장 큰 수를 max()로 불러온다.

#강사님 코드
# 1.split()함수를 활용하여
words = sentence.split()
print(words)
# 가장 긴 단어를 words 리스트를 순회 비교

longWord = words[0]
for w in words:
    if len(longWord) < len(w) :
        longWord = w
print(len(words), longWord)
print()

# max()함수를 이용.

print(len(max(words)),max(words))

print()
lengths = [len(w) for w in words]

longest = words[lengths.index(max(lengths))]
print(len(words),longest)