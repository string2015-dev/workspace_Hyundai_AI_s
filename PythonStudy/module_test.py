# import calc.basic , calc.advanced

# print(calc.basic.add(3,7))
# print(calc.advanced.multiply(3,10))
#=====================================
# 지금은 나눠진 모듈 별로 가지고와서 사용함.
# 더 큰 패키지 범위로 가지고 오고 싶다면.
# 모듈을 만들어둔 dir의 init을 변경한다!
# import calc 로 불러온다
#========================================
# 다른 방법
# init 파일에 __all__ = ["모듈파일명"]
# from calc import *
# print(calc.basic.add(3,7))
# print(calc.advanced.multiply(3,10))

# 또 다른 방법
# init 파일에 from 패키지.모듈 import *
import calc
print(calc.add(3,7))