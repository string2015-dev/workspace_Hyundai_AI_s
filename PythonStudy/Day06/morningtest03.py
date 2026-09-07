# 1부터 20까지의 숫자 중 짝수는 even_list, 
# 홀수는 odd_list에 각각 담아 출력하세요. (if / else 사용)

odd_list =[]
even_list = []
for i in range(1,21):
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(f"짝수: {even_list} / 홀수: {odd_list}")