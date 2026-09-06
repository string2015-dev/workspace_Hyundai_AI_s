# 5 딕셔너리 순회하며 출력하기
character = {"name": "기사", "hp": 200, "mp": 30, "level": 5}
for key in character:
    print('"{}: {}"'.format(key,character[key]))

# movie 딕셔너리를 생성하고 위 각각 담아 놓은 5개의 데이터를 movie에 저장하세요 
# for사용X
movie = {}
movie["name"] = "기사"
movie["hp"] = 200
print(f"{movie['hp']}")

for key, value in movie.items():
    print("{}{}".format(key,value))