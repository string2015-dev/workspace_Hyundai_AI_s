student = {"이름": "김클라라", 
           "나이": 25, 
           "전공": "컴퓨터공학"}
student_list=[f"{name} : 전공{score}" for name,score in student.items()]
print(*student_list)