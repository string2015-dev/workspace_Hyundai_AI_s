# str1 ="aaaaa"
# str2 = "bbbbb"
# str_origin1 = [s1 for s1 in str1]
# str_origin2 = [s2 for s2 in str2]
# new_str = "".join([str_origin1[i]+str_origin2[i] for i in range(len(str1))])
# # for i in range(len(str1)):
# #     new_str += str_origin1[i], str_origin2[i]

# print("".join(new_str))

# def solution(a, b):
#     a = str(a)
#     b = str(b)
#     row1 = a+b
#     row2 = b+a
#     row1 = int(row1)
#     row2 = int(row2)
#     if row1 > row2:
#         return(row1)
#     else: return(row2)
# ====================================
# a=int(input())
# b=int(input())
# sum = f"{a}{b}" 
# int(f"{a}{b}") if int(f"{a}{b}") >= 2*a*b else 2*a*b
# ====================================
# 정수 num과 n이 매개 변수로 num이 n의 배수면 1 아니면 0
# 1 if num%n == 0 else 0
# ======================================
# 정수 number와 n, m이 주어질때 number가 n의 배수이면서 m의 배수면 1 아님 0
# 1 if number % n==0 and number% m==0 else 0
#=======================================
#홀짝에 따라 다른 값 반환
# 양의 정수 n이 매개변수로 주어질떄 n이 홀수면 n 이하의 홀수인 모든 양의 정수의 합을
# return n이 짝수람녀 n이하의 짝수인 모든 양의 정수의 제곱의 합 return하는 함수.
# sum(i**2 for i in range(1,n+1) if i%2==0 ) if n%2 == 0 else sum(i for i in range(1,n+1) if i%2!=0)
#=======================================
# 조건 문자열
# 두 수가 n과 m. ineq 는 < ,> 중 하나 eq는 =, !중 하나
# 1 if bool(n eval(ineq+eq) m) else 0 이거는 어떻게 하면 가능할까.....
    # if eq == "=":
    #     return int(n >= m if ineq == ">" else n <= m)
    # else:
    #     return int(n > m if ineq == ">" else n < m)
#=======================================
# flag에 따라 다른 값 반환하기
# 정수 a,b와 boolean변수 flag가 매개 변수로 주어질때
# flag가 True면 a+b, False면 a-b 함수
# a+b if flag else a-b
#=======================================
# 코드 처리하기
# 문자열 code를 앞에서 읽으며 "1"이면 mode를 바꿉니다.
# mode에 따라 code를 읽어가면서 문자열 ret을 만들어 냅니다.
