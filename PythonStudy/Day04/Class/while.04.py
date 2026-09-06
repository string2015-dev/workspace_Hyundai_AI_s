# import time.time()   # 예: 1557241486.6654928
# while_with_time.py
# 시간과 관련된 기능을 가져옵니다.
import time

# 변수를 선언합니다.
number = 0

# 5초 동안 반복합니다.
target_tick = time.time() + 5

while time.time() < target_tick:
    number += 1
    # 출력합니다.
    print("5초 동안{}번 반복했습니다.".format(number))
    # 예: 5초 동안 14223967번 반복했습니다.