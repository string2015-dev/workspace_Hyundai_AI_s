dictionary = {    "name": "7D 건조 망고",    "type": "당절임",    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],    "origin": "필리핀"}

#사용자에게 입력을 받습니다.(key)
key = input("제품 항목을 입력하세요> ")
if key in dictionary :
    print(dictionary[key])
else:
    print("존재하지 않는 키입니다.")