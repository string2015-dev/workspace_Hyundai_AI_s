#현재 시간을 시스템으로 부터 가지고 와서 오전 오후로 나누는 프로그램을 만든다.
# 오전, 오후의 기준은 12시로 정한다.

import datetime

now = datetime.datetime.now()

if now.hour == 12 :
    print("정오")
elif now.hour < 12 :
    print("오전")
else:
    print("오후")

if now.hour == 12 :
    print("{}시 정오입니다.".format(now.hour))
    