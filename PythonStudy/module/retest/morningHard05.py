#### 5. 간단한 To-Do 리스트 관리 프로그램 — `[종합: 함수 + while + 데이터구조 + 제어문]`
# - **시나리오**: 사용자가 메뉴를 선택해 할 일을 추가/삭제/조회하는 콘솔 프로그램입니다.
# - **요구사항**:
#     1. `while` 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#     2. 각 기능을 함수로 분리: `add_task()`, `delete_task()`, `show_tasks()`
#     3. 할 일 목록은 리스트에 저장, 완료 여부는 딕셔너리(`{"할일": "장보기", "완료": False}`)로 관리
#======================================================================
tasks = []
def add_task(task):
    tasks.append({"할일":task, "완료":False})

def delet_task(index):
    if 0 <= index <len(tasks):
        removed = tasks.pop(index)
        print(f"{removed["할일"]} 삭제완료")
    else: print("잘못된 번호 입니다.")

def show_tasks():
    if not tasks:
        print("목록이 비어있습니다.")
    for i, task in enumerate(tasks):
        status = "완료" if task["완료"] else "미완료"
        print(f"{i}. {task["할일"]} [{status}]")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["완료"] = True
    else: print("잘못된 번호 입니다.")
#==================================================================
def Todo_run():
    while True:
        print("\n[메뉴] 1.추가 2.삭제 3.완료처리 4.전체조회 5.종료")
        choice = input("메뉴 번호를 선택하세요")
        if choice == "1":
            add_task(input("할 일을 입력하세요: "))
        elif choice == "2":
            delet_task(int(input("삭제할 번호: ")))
        elif choice =="3":
            complete_task(int(input("완료한 할 일 번호: ")))
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            Print("프로그램을 종료합니다.")
            break
        else: print("1-5번의 메뉴번호를 선택하세요")
Todo_run()