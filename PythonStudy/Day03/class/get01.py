dictionary = {    "name": "7D 건조 망고",    "type": "당절임",    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],    "origin": "필리핀"}

# 존재하지 않는 키에 접근해 봅니다.
value = dictionary.get("존재하지 않는 키")

print("값:", value)
# None 확인 방법
if value == None:
     # None과 같은지 확인만 하면 됩니다.
    print("존재하지 않는 키에 접근했습니다.")

dictionary.get()