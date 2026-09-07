def get_input(prompt, value):
    try:
        return input(prompt)
    except EOFError:
        print(f"입력처리 불가 - {value} 기본 값으로 진행합니다.")
        return value

#======================================================================
#[응용 1] 학생 성적 관리 시스템
# - **시나리오**: 여러 학생의 정보를 리스트 안의 딕셔너리로 관리합니다.
# - **요구사항**:
#     1. 학생을 추가하는 함수 `add_student(name, score)`
#     2. 전체 평균을 구하는 함수 `get_average()`
#     3. 평균 이상인 학생만 출력하는 함수 `get_top_students()`
#   students = [      {"이름": "김클라라", "점수": 90},      {"이름": "이개발", "점수": 75},  ]
students = [      {"이름": "김클라라", "점수": 90},      
            {"이름": "이개발", "점수": 75},  ]

def add_student(name, score):
    students.append({"이름":name, "점수":score})

def get_average():
    if not students:
            return 0
    total = 0
    averageValue = 0.0
    for student in students:
    # 한 학생의 정보는 student라는 딕셔너리로 관리하고, 학생 한명당 정보를 가지고 있다.
    # 전체 학생은 students라는 리스트로 관리한다.
        total += student["점수"]
        # 전체 학생들 점수 합계를 구하는 로직 
    averageValue = total/len(students)
    return averageValue

def get_top_students(): #평균 점수 이상인 학생들만 새 리스트에 반환하는 함수
     avg = get_average()
     return [s for s in students if s["점수"] >= avg]
add_student("서유미",80)
print(f"평균점수: {get_average():.1f}")
print(f"평균 이상 우수 학생: {get_top_students()}")
#======================================================================
#[응용2] 온라인 쇼핑몰 장바구니 계산기
# - **시나리오**: 장바구니에 담긴 상품(이름, 가격, 수량)의 총 결제금액을 계산합니다.
# 1. 총 금액을 계산하는 함수 `calculate_total(cart)`
# 2. 총 금액이 **50,000원 이상이면 10% 할인**을 적용하는 조건문 추가
# 3. 최종 결제 금액 출력
cart = [      {"상품명": "키보드", "가격": 50000, "수량": 1},      
          {"상품명": "마우스", "가격": 20000, "수량": 2},  ]
print("=====응용 문제 2 장바구니 구현=====")
def calculate_tatal(cart):
    #딕셔너리 리스트를 받아서 할인 전 총금액 계산하기
    total = 0
    # total = sum(item["가격"]*item["수량"] for item in cart)
    for item in cart:
         total += item["가격"]*item["수량"]
         #for문이 돌고 나면 total에 할인 전 총 금액이 들어간다.
    return total
def apply_discount(total):
     if total >= 50000:
        discount = total*0.9 # 50000원 이상 되면 할인 해줘라
        return discount
     return discount # 50,000원 안 넘으면 그대로 출력해라.

print("cart 실행")
subtotal = calculate_tatal(cart)
final_price = apply_discount(subtotal)

print(f"할인전 금액: {subtotal: ,}원 \n최종 결제 금액: {final_price: ,.0f}원")

#======================================================================
#[응용3] 회원 등급 필터링 시스템
# - **시나리오**: 회원 목록에서 나이/구매금액 조건에 맞는 회원만 뽑아 등급을 부여합니다.
# - **요구사항**:
#     1. 구매금액이 100만원 이상이면 "VIP", 50만원 이상이면 "일반", 
#           그 미만이면 "신규"로 등급을 매기는 함수 `get_grade(amount)`
#     2. 회원 리스트를 순회하며 각 회원의 등급을 딕셔너리에 추가
#     3. "VIP" 등급 회원만 따로 리스트로 출력
print("=====응용3 회원 등급 필터링 시스템=====")
members = [
     {"이름": "김부자","구매금액":500000000, "나이":10, "등급":"vip"},
     {"이름": "이서민", "구매금액":600000, "등급":"일반"},
     {"이름": "박중산", "구매금액":20000,"등급":"신규"},
]
#구매 금액에 따른 등급 문자열을 반환하는 함수
def get_grade(amount):
     if amount >= 1000000:
          return "vip"
     elif amount >= 500000:
          return "일반"
     else:
          return "신규"
#회원 리스트를 순회하면서, 각 딕셔너리에 "등급" key 새로 추가
for member in members:
     member["등급"] = get_grade(member["구매금액"])
#회원의 전체 목록 출력
print(f"등급이 매겨진 회원 목록: {members}")

vip_members = [m for m in members if m["등급"] == "vip"]
print(f"vip 회원 리스트: {vip_members}")
#======================================================================
#[응용4] 텍스트 단어 빈도수 분석기
# - **시나리오**: 긴 문장(예: 리뷰 텍스트)에서 각 단어가 몇 번 등장하는지 세는 프로그램을 만듭니다.
# 1. 공백 기준으로 단어를 나누고(`split()`), 딕셔너리에 `{단어: 등장횟수}` 형태로 저장
# 2. 가장 많이 등장한 단어 TOP 3을 출력
text = "이 제품 정말 좋아요 배송도 빠르고 품질도 좋아요"
print("=====응용 문제4 텍스트 단어 빈도수 분석기=====")
#=====================================================================
# 스플릿으로 단어 단위로 split 리스트를 잡고 리스트의 값을 key로 삼아서 딕셔너리를 만든다.
# 이때 for문을 이용해서 처음 split 리스트에서 겹치는 단어의 빈도를 뽑아낸다.
# 딕셔너리 key: 빈도를 추가해서 딕셔너리를 완성한다.
#=====================================================================
# word_list = text.split()
# for i in range(len(word_list)):
#      if 

# 1. 문장을 쪼갠후, {단어:횟수} 구성하여 반환하는 함수
def count_word(sentence):
     words = sentence.split() # split() 공백을 기준으로 문자열을 리스트로 반환
     counts ={}
     for word in words:
          #dict.get(key, 기본값) : key가 존재한다면 해당 값을 리턴, 없으면 기본 값 0 을 리턴
          counts[word] = counts.get(word,0) + 1
     return counts

word_count = count_word(text)

# 2. 내림차순 정렬: 가장 많이 등장하는 단어 TOP3
sorted_words = sorted(word_count.items(), key=lambda x:x[1], reverse=True)

top3 = sorted_words[:3]

# 3. 슬라이싱 한 것을 출력한다.(텍스트를 (벡터숫자)횟수로 바꾸는 과정=> 임베딩)
print(top3)

#======================================================================
#[응용5] 간단한 To-Do 리스트 관리 프로그램
# - **시나리오**: 사용자가 메뉴를 선택해 할 일을 추가/삭제/조회하는 콘솔 프로그램입니다.
# - **요구사항**:
#     1. `while` 반복문으로 프로그램이 계속 실행되도록 메뉴(추가/삭제/조회/종료)를 반복 출력
#     2. 각 기능을 함수로 분리: `add_task()`, `delete_task()`, `show_tasks()`
#     3. 할 일 목록은 리스트에 저장, 완료 여부는 딕셔너리(`{"할일": "장보기", "완료": False}`)로 관리
print("=====간단한 To-Do 리스트 관리 프로그램======")

tasks = [] #{"할일":str, "완료":bool}

def add_task(task):
    tasks.append({"할일":task, "완료":False})

def delete_task(index):
    if 0 <= index < len(tasks):
            removed = task.pop(index)
            print(f"'{removed["할일"]}'삭제완료")
    else:
        print("잘못된 번호입니다.")

def complete_task(index):
     if 0<= index < len(tasks):
          tasks[index]["완료"] = True
def show_tasks():
     if not tasks:
          print("할일 목록이 비어있습니다.")
          return
     for i,task in enumerate(tasks):
          status = "완료" if task["완료"] else "미완료"
          print(f"{i}.{task["할일"]} [{status}]")
def todo_run():
     while True:

          print("\n[메뉴] 1.추가 2.삭제 3.완료처리 4.전체조회 5.종료")
          choice = get_input("메뉴 번호 선택> ","5")
          if choice == "1":
               name =get_input("할 일을 입력하세요: ", "예: 할일")
               add_task(name)
          elif choice =="2":
               idx = get_input("삭제할 번호: ", "0")
               delete_task(ini(idx))
          elif choice == "3":
               idx = get_input("완료 처리 번호 입력> ", "0")
               complete_task(int(idx))
          elif choice == "4":
               show_tasks()
          elif choice == "5":
               print("Todo 프로그램 종료")
               break
          else:
               print("메뉴 번호는 1-5번 까지 입니다.")
todo_run()