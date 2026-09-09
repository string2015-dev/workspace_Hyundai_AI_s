#### 1. 학생 성적 관리 시스템 — `[딕셔너리 + 리스트 + 함수 + 반복문]`
# - **시나리오**: 여러 학생의 정보를 리스트 안의 딕셔너리로 관리합니다.
# students = [      {"이름": "김클라라", "점수": 90},      {"이름": "이개발", "점수": 75},  ]
# - **요구사항**:
#     1. 학생을 추가하는 함수 `add_student(name, score)`
#     2. 전체 평균을 구하는 함수 `get_average()`
#     3. 평균 이상인 학생만 출력하는 함수 `get_top_students()`
# - 🎯 **포인트**: "왜 리스트 안에 딕셔너리를 썼는가?"를 README에 설명할 수 있어야 합니다.
#======================================================================
students = [      {"이름": "김클라라", "점수": 90},      {"이름": "이개발", "점수": 75},  ]
#1. 학생 추가하는 함수.
def add_student(name,score):
    students.append({"이름":name, "점수": score})
#2. 전체 평균을 구하는 함수.
def get_average():
    total_score = sum([student["점수"] for student in students])
    average_score = total_score / len(students)
    return average_score
#3. 평균 이상인 학생만 출력하는 함수
def get_top_students():
    top_students = [student["이름"] for student in students if student["점수"] >= get_average()]
    return top_students

print(add_student("항수", 86))
print(get_average())
print(get_top_students())