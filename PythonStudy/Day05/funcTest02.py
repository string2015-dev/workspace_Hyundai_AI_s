#문자열 앞뒤 공백 제거하기
text = "   Python Programming   "

string = text.strip()
print(f"{len(text)}공백제거전 {len(string)}공백 제거 후 길이 입니다.")