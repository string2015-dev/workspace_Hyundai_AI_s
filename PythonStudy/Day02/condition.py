# 입력을 받습니다.
data  = input('숫자를 입력해 주세요')
data  = int(data) # 입력받은 문자열을 정수로 변환합니다.

# 양수 조건if number > 0:    print("양수입니다")
if data > 0:
    print('양수')

# 음수 조건if number < 0:    print("음수입니다")
if data < 0:
    print('음수')

# 0 조건if number == 0:      print("0입니다")
if data == 0:
    print('0')

number = input("숫자 입력해 주세요 > ")
number = int(number) # 문자열 => 숫자(형변환) => 캐스팅 ,입력받은 문자열을 정수로 변환합니다.
if number == 0 :
    print('0 이네요!')
elif number > 0 :
    print('양수')
elif number < 0 :
    print('음수')
else:
    print('처리 불가')
    