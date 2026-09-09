def call_10_times(func): #콜백 함수
    for i in range(10):
        func()

def print_hello():
    print("hello!")
call_10_times(print_hello)
#====================================================================
