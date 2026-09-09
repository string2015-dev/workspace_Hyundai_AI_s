# 튜플은 함수의 return에 많이 사용된다.
# 왜냐하면 return에 여러 값을 다양하게 전달 할 수 있기 때문.

# test함수 선언하고 함수는 return값으로 10, 20 두개의 정수를 리턴.
def test_f2():
    return 100
def test_f():
    return (10,20)
def test_f1():
    return 30,40

print(test_f2())
print(test_f())
print(test_f1())

a,b = test_f1()
print(a)
print(b)
print()
print("==실무 예제 for enumerate()==")

for i, value in enumerate([1,2,3,4,5,6]):
    print(f"{i+1}번째 요소는{value}입니다.")