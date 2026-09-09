#### 4. 텍스트 단어 빈도수 분석기 — `[딕셔너리 + 반복문 + 함수]`
# - **시나리오**: 긴 문장(예: 리뷰 텍스트)에서 각 단어가 몇 번 등장하는지 세는 프로그램을 만듭니다.
# 텍스트를 숫자로 바꾸는 ‘임베딩’부터 진행한다.
# - **요구사항**:
#     1. 공백 기준으로 단어를 나누고(`split()`), 딕셔너리에 `{단어: 등장횟수}` 형태로 저장
#     2. 가장 많이 등장한 단어 TOP 3을 출력
# - 💡 **연결고리**: 이 문제는 임베딩(문장을 숫자로 바꾸는 것)이나 RAG(문서 검색 기반 AI 응답)의 아주 첫걸음이에요. "컴퓨터가 텍스트를 이해하려면 결국 숫자로 세는 것부터 시작한다"는 감각을 여기서 미리 잡아줄 수 있습니다.
#======================================================================
text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"
#1. 공백 기준 단어를 딕셔너리형태로 저장.
words = text.split()
# words라는 리스트로 저장.
# 빈  딕셔너리 만들기
diction ={}
for word in words:
    if word not in diction:
        diction[word] = 1
    else:
        diction[word] += 1
print(diction)
#2. 가장 많이 등장하는 단어 Top3 정렬
top_sorted = [(key,value) for key,value in diction.items()]

sorted_list = sorted(top_sorted, key=lambda x: x[1], reverse=True)
top3 = sorted_list[:3]
print(top3)