# #12 FizzBuzz 문제
# 1부터 30까지 숫자를 출력하되, 
# 3의 배수면 "Fizz", 
# 5의 배수면 "Buzz", 둘 다의 배수면 "FizzBuzz"를 출력해보세요.

for i in range(1,31):
    
    if i%3 == 0 and i%5 == 0:
        print(f'{i} 3과 5의 공배수입니다. "FizzBuzz"')
    elif i%3 == 0:
        print('{} 3의 배수입니다. "Fizz"'.format(i))
    elif i%5 == 0:
        print(f'{i} 5의 배수입니다."Buzz"')
    else:
        print(i)

