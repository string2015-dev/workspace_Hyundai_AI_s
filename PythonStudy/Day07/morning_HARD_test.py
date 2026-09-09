#### 5. 간단한 To-Do 리스트 관리 프로그램 — `[종합: 함수 + while + 데이터구조 + 제어문]`
# - **시나리오**: 사용자가 메뉴를 선택해 할 일을 추가/삭제/조회하는 콘솔 프로그램입니다.
# - **요구사항**:
#     1. `while` 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#     2. 각 기능을 함수로 분리: `add_task()`, `delete_task()`, `show_tasks()`
#     3. 할 일 목록은 리스트에 저장, 
#       완료 여부는 딕셔너리(`{"할일": "장보기", "완료": False}`)로 관리
#======================================================================
tasks =[]
#할 일을 더하는 함수
def add_task(task):
    tasks.append({"할일":task, "완료":False})
#할일을 삭제하는 함수
def remove_task(index):
    if 0 <= index < len(tasks):
        print(f"{tasks[index]["할일"]}을 삭제했습니다.")
        removed = tasks.pop(index)
        
    else: print("잘못된 번호입니다.")
#할일을 완료처리하는 함수
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["완료"] = True
    else: print("잘못된 번호입니다.")
#할일 리스트 조회하는 함수
def show_task():
    if not tasks:
        print("할일 목록이 비어있습니다.")
        return
    for i,task in enumerate(tasks):
        status = "완료" if task["완료"] else "미완료"
        print(f"{i}.{task["할일"]} [{status}]")
    # if 0<= i < len(tasks):
    #     ident = "완료" if tasks[i]["완료"] else "미완료"
    #     print(f"{i}. {tasks[i]["할일"]} 완료여부: {ident}")
    # else: print("할일이 없습니다.")
#======================================================================

def todo_run():
    while True:
        print("\n[메뉴] 1.할일추가 2.할일삭제 3.할일완료 4.할일목록 5.종료")
        choice = input()
        if choice == "1":
            add_task(input("할일을 입력하세요 > "))
        elif choice == "2":
            remove_task(int(input("삭제할 할일 번호 > ")))
        elif choice == "3":
            complete_task(int(input("완료한 할일 번호 > ")))
        elif choice == "4":
            show_task()
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else: print("잘못된번호입니다.")
todo_run()