list_of_list = [    [1, 2, 3],    [4, 5, 6, 7],    [8, 9]]
for items in list_of_list:
    print(items)
print()
# 위의 코드대로 진행하면 제일 외각의 리스트안의 데이터를 가지고왔다
# 내부 리스트의 데이터에 접근하기위해서 for문을 한 번 더 사용해야한다.
list_of_list = [    [1, 2, 3],    [4, 5, 6, 7],    [8, 9]]
for items in list_of_list:
    for item in items:
        print(item)
print()
#위의 코드
#첫번쨰 줄 for문을 통해서 [123]를 items에 담는다.
#두번쨰 줄 for문을 통해서 [123]의 1을 item에 담고 print(item)으로 출력한다.
#[4557]의 4,5,6,7을 뽑아낸다. [89]의 [8,9]를 뽑아낸다.
list_of_list = [    [1, 2, 3],    [4, 5, 6, 7],    [8, 9]]
for items in list_of_list:
    for item in items:
        print(items)
#위의 코드
# 첫번째 줄 for문을 통해서 [123]을 items에 담는다.
# 두번째 줄 for문을 통해서 item에 [1]을 담는다.
# 세번쨰 print(items)를 통해 [123]을 출력한다.
#위 반복.
