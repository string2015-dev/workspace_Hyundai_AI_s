# 문제 1 리스트 합계 구하기
`sum()` 함수를 사용하지 않고, 반복문으로 리스트의 합계를 구해보세요.

numbers = [12, 25, 7, 33, 18]
# 여기를 채워보세요
합계 = 0
for i in numbers:
    합계 += i
print(합계)

# 문제 2 리스트 평균 구하기
문제1 로직을 응응해 평균을 구해보세요.
평균 = 합계 / len(numbers)
print(평균)

# 문제 14 두 리스트로 딕셔너리 만들기(range 활용)
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

result = {}
for in in range(len(key_list)):
    result[key_list[i]] = value_list[i]     
** result라는 딕셔너리에 key_list[i]의 데이터를 "키" 지정을 하고 value_list[i]의 데이터를 "값"으로 지정한다. **
** 즉 같은 인덱스를 가진 데이터를 '키' : '값' 매핑한다. **
print(result)

# 문제 13 짝수만 필터링 해서 새 리스트 만들기
