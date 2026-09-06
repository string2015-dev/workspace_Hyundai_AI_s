# 중첩 반복문으로 피라미드 만들기
# for_pyramid02.py
output = ""

for i in range(1, 15):
    for j in range(14, i, -1):
        output += ' '
        for k in range(0, 2 * i - 1):
            output += '*'
            output += '\n'
print(output)