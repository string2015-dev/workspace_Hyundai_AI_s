#1 학생 성적 관리 시스템. 틱셔너리+리스트+함수+반복문
students = [      {"이름": "김클라라", "점수": 90},      
              {"이름": "이개발", "점수": 75},  ]

# 1. 학생을 추가하는 함수 `add_student(name, score)
def add_student (data_list,name,score):
    data_list.append({"이름":name,"점수":score})

# 2. 전체 평균을 구하는 함수 `get_average()`
def get_average(data_list):
    if not data_list:
        return 0
    elif data_list:
        total = sum(student["점수"] for student in data_list)
        average = total/len(data_list)
        return average

# 3. 평균 이상인 학생만 출력하는 함수 `get_top_students()
def get_top_students(data_list):
    total = sum(student["점수"] for student in data_list)
    average = get_average(data_list)
    top_students = [student["이름"] for student in data_list if student["점수"] >= average]
    return top_students

    # average = total/len(data_list)
    # students_list = [student["점수"] for student in data_list]
    # over = []
    # for i in range(students_list):
    #     if average <= students_list[i]:
    #         over.append(i)
    #     else: return ("평균이상이 없습니다.")

    




add_student(students,"박프로그래머",88)
print(students)
print()
print(f"{get_average(students):.2f}")
print()
print(get_top_students(students))