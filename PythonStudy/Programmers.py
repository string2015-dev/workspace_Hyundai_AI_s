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

#=====
# 코드처리하기
#문자열이 주어지고 "1"을 만나면 mode를 바꾼다.
# mode = 0
# code = "abc1abc1abc"
# ret = ""

# for i in range(len(code)):
#     if mode == 0:
#         if code[i] != "1":
#             if i%2==0:
#                 ret += code[i]
#         else:
#             mode = 1

#     elif mode == 1:
#         if code[i] != "1":
#             if i%2 !=0:
#                 ret +=code[i]
#         else:
#             mode = 0
# if not ret:
#     print("EMPTY")
# print(ret)
#===================================================================
# 등차 수열의 특정한 항만 더하기
# 정수 a,b 길이가n인 boolean배열 included주어진다.
# 첫항이 a, 공차가 d 인 등차수열에서 inclued[i]가 i+1항일때
# True 인 항들만 더한 값을 return 하는 solution 함수

# total = sum(a+d*i for i in range(len(included)) if included[i])
#===================================================================
# 주사위게임2
# 1~6까지 있는 주사위 세개 값을 각각 a, b, c 라고 할때.
# 점수가 다 다르면 a+b+c
# 하나만 다르면 (a+b+c)*(a**2+b**2+c**2)
# 셋다 같으면 (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
# if a == b == c:
#     return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
# elif len({a,b,c}) == 3:
#     return a+b+c
# else: (a+b+c)*(a**2+b**2+c**2)
#===================================================================
#정수가 담신 num_list가 주어질때 
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1 크면 0 return
# num_list = [3,4,5,2,1]
# total = sum(num for num in num_list)

# # sque = *num_list
# sque = "*".join(map(str,num_list))
# eval(sque)
# print(sum(num_list))
#===================================================================
#이어 붙인 수
# 정수리스트 num_list에서 리스트의 홀수만 이어붙인 수와 짝수만 이어붙인 수
# 의 합을 return하라.
# num_list =[3, 4, 5, 2, 1]
# # odd_list = [i for i in num_list if i%2 !=0]
# # even_list = [i for i in num_list if i%2 ==0]

# sum_list = int("".join(map(str,filter(lambda x : x%2 !=0,num_list)))) + int("".join(map(str,filter(lambda x : x%2==0, num_list))))
# print(sum_list)
#=====================================================================
# 마지막 두 원소
# 정수리스트 num_list 마지막 원소가 그 전 원소보다 크면 마지막 원소-그전원소
# 마지막원소 <= 그전원소: 마지막원소*2 return 하시오.
# num_list = [5, 2, 1, 7, 5]
# num_list2= sorted(list(enumerate(num_list)),reverse = True)
# if num_list2[0][1]>num_list2[1][1]:
#     num_list.append(num_list2[0][1]-num_list2[1][1])
# else: num_list.append(num_list2[0][1]*2)
# print(num_list)
#=====================================================================
#수 조작하기1
# 정수 n 문자열 control은 w,a,s,d로 이루어져있으며 각 값이 나올때 마다 n의 값을 바꾼다.
# control의 앞에서 부터 읽어 나갈때 규칙에 따라 n의 값이 어떻게 되는지?
# control = "wsdawsdassw"
# n = 0

# for i in control:
#     if i == "w":
#         n+=1
#     elif i == "s":
#         n-=1
#     elif i =="d":
#         n+=10
#     else: n-=10
# print(n)
#====================================================================
# 수 조작하기2
# 정수 배열 numlog
# numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
# print(list(enumerate(numLog)))
# 즉 0번째 0부터 시작
# for a, value in enumerate(numlog):
#     print(f"{a}번째 결과: {value}")
# # "w" = numlog[i] +1
# # "s" = numlog[i] -1
# # "d" = numlog[i] +10
# # "a" = numlog[i] -10
# # for i in range(numlog):
# #     numlog[i] = numlog[0]
# print(numlog[-1::-1])
# for value in numlog[-1::-1]:
#     print(value)
# words = ""
# rev = list(numLog)
# for i in range(len(numLog)-1):
#     if rev[i]-rev[i+1] == 1:
#         words+="s"
#     elif rev[i]-rev[i+1] == -1:
#         words+="w"
#     elif rev[i]-rev[i+1] == 10:
#         words+="a"
#     elif rev[i]-rev[i+1] ==-10:
#         words +="d"
# answer = reversed(words)
# print(words)
#======================================================================
# 정수 배열 arr과 2차원 정수배열 queries 쿼리스의 원소 쿼리는 [i,j]꼴
# 각 쿼리마다 순서대로 arr[i] 값과 arr[j]을 서로 바꿉니다.
# arr = [0, 1, 2, 3, 4]
# queries =[[0, 3],[1, 2],[1, 4]]
# [3, 4, 1, 0, 2]
# array =list(enumerate(arr))

# for i in queries:
#     arr[i[0]],arr[i[1]] = arr[i[1]],arr[i[0]]

# print(arr)
#=====================================================================
#수열과 구간 쿼리2
# 정수 배열 arr 2차원 정수 배열 querise의 원소를 query [s,e,k]
# 쿼리마다 순서대로 s<= i<= e 인 모든 i에 대해 k보다 크면서 가장 작은 arr[i] 찾으시오
# 쿼리 답이 없으면 -1 출력
# arr =[0, 1, 2, 4, 3]
# queries =[[0, 4, 2],[0, 3, 2],[0, 2, 2]]
# result = [3, 4, -1]
# result =[]
# for i in queries:
#     for j in arr:
#         if i[0]<= j <=i[1] and i[2]<j :
#             min()
# result = []
# for s,e,k in queries:
# #     array =[i for i in range(len(arr)) if s<= i <=e and i>k]
# #     if not min(array):
# #         result.append(arr[-1])
# #     else: result.append(arr[min(array)])
# # print(result)
#     array = []
#     array = [arr[i] for i in range(len(arr)) if s<= i <=e and arr[i] > k]
#     if not array:
#         result.append(-1)
#     else: result.append(min(array))
# print(result)
#==================================================================
# 정수 배역 arr 2차원 정수 배열 queries query = [sek]
# s<= i <= e 인 모든 i중 k의 배수면 arr[i]에 1 더합니다.
# 쿼리스 처리 후 arr 리턴 함수
# arr= [0, 1, 2, 4, 3]
# queries =[[0, 4, 1],[0, 3, 2],[0, 3, 3]]
# arr =[3, 2, 4, 6, 4]
# arr =[0,1,2,4,3]
# for s,e,k in queries:
#     for i in range(len(arr)):
#         if s <= i <=e and i % k == 0:
#             arr[i]+=1
# print(arr)
#=================================================================
#정수 L과 R이 주어졌을때, l이상 r이하의 정수 중에서 숫자 0과 5로만 이루어진 모든
# 정수를 오름차순으로 저장한 배열을 return하는 solution 함수를 완성해주세요.
# 그런 정수가 없다면 -1 담긴 배열을 return 합니다.

# 숫자 0과 5로만 이루어진 수를 어떻게 만들 수 있을까?

# 0, 5, 
# 50, 55, 
# 500, 505, 550, 555, 
# 5000, 5005, 5050, 5500, 5055, 5550, 5505, 5555
# 50000, 50005, 50055, 50550, 55500,

# 배열 만들기 2
# l = 5
# r = 555
# # list_test =[]
# # list_test2 =[]
# # temp=[]
# answer = []
# # for i in range(l,r+1):
# #     list_test.append(str(i))
# # for j in list_test:
# #     if j == '5' or j =='0':
# #         list_test2.append(j)
# for i in range(l,r+1):
#     zero_five = str(i)
#     if set(zero_five) <= {'0','5'}:
#         zero_five=int(zero_five)
#         answer.append(zero_five)
#     if not answer:
#         answer =-1
# print(answer)
#=====================================================================
#