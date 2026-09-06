# 점수 기준으로 내림차순 정렬하기
scores = [("철수", 85), ("영희", 92), ("민수", 78)]
dict_scores = []

a = len(scores)
# print(a)  scores에는 3개의 요소가 있음.
# ('철수', 85) 으로 데이터가 들어감.


# 강사님 코드
# 1단계 딕셔너리로 재구성한다. (dic()이라는 생성자를 이용해서.)
scores_dic = dict(scores)
print(scores_dic)
# 2단계 items활용하여 점수값 기준으로 내림차순 정렬
def get_score(item):    # item: 매개변수
    return item[1]      # 1: 하나의 값을 받아 비교후 처리해주겠다.

scores_dic = dict(scores_dic.items(), key = get_score,reverse=True)
print(scores_dic)
# 함수를 선언하면 이름을 불러서 동작하게 한다.


# val = scores_dic.values()
# print(type(val))