# ### 문제 4. 자료형을 구분해서 출력하기 (type() 활용)
# 파이썬은 다음과 같은 방법으로 특정 값이 어떤 자료형인지 확인할 수 있습니다.

# 딕셔너리를 선언합니다.
character = {    "name": "기사",    
             "level": 12,    
             "items": {        "sword": "불꽃의 검",        "armor": "풀플레이트"    },    
             "skill": ["베기", "세계 베기", "아주 세계 베기"]}
 
# for 반복문을 사용합니다.
for key in character:
    T = character[key]
    if type(T) == list:
        skills = T
        for skill in skills:
            print(key, " : ", skill)
    elif type(T) == dict:
        items = T
        for key in items:
            print(key, " : ", items[key])
    else:
        print(key, " : ", T)


#강사님 코드
character = {    "name": "기사",    "level": 12,    "items": {        "sword": "불꽃의 검",        "armor": "풀플레이트"    },    "skill": ["베기", "세계 베기", "아주 세계 베기"]}
for key in character:
    if type(character[key]) is dict:
            for inner_key in character[key]:
                        print(inner_key, ":", character[key][inner_key])
    elif type(character[key]) is list:
                                    for item in character[key]:
                                                print(key, ":", item)
    else:
                                                            print(key, ":", character[key])
