# 10 단어별 등장 횟수 세기(빈도수 계산)
# 유사도 검사를 진행할때 중요함. <- 어떻게 중요하지?
#
text = "apple banana apple cherry banana apple"
#강의
# 1. count = 딕셔너리 생성
count = {}
# 2. 문자열에서 공백을 기준으로 단어를 분리 split
# => 리스트로 생성한다.
words = text.split()
#3. 분리된 단어별 횟수를 센다
    # 논리생각: 단어가 처음 나왔을때만 True로 작동하는 리스트를 만들어 같은 단어를 담는다.
    # 리스트의 길이를 세면 단어 등장 빈도를 알 수 있고
    # 단어를 키로 리스트의 길이를 값으로 지정하면 완성!
for w in words:
    if w in count:
        count[w] = count[w] + 1
    else: count[w] = 1 
#4. count 딕셔너리 출력
print(count)