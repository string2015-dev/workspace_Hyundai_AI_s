# 문자열 나누고 다시 합치기
sentence = "사과,바나나,포도,딸기"
strr = ""
spl = sentence.split(",")

for i in range(0,len(sentence)):
    strr += sentence[i]
print(strr,sep = " - ")    
print(strr.replace(","," - "))
# spl = [사과, 바나나, 포도, 딸기]

# 8번째 줄에서 
# sep = " - " 이게 띄워쓰기를 " - "로 바꾼다는거죠?
# 문장에서 ","를 " - "로 바꿨어야 했어서 작동을 안한거였어!!

# 강사님 코드
sliceFruit = sentence.split(",")
#split은 ()의 구분자로 구분해서 잘라내라 라는 뜻.
result = " - ".join(sliceFruit)
print(result)