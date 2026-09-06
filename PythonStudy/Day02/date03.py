#계절을 구분하는 프로그램

import datetime
now = datetime.datetime.now()

if 2 < now.month < 6 :
    print("{}월은 봄입니다.".format(now.month))
elif 6 <= now.month < 9:
    print("{}월은 여름입니다.".format(now.month))
elif 9 <= now.month < 12:
    print("{}월은 가을입니다.".format(now.month))
else:
    print("{}월은 겨울입니다.".format(now.month))