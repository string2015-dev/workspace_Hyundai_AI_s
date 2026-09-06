#1 len() 함수
name = "AI개발자"
print(len(name))  # 출력: 5  (한 글자당 1개씩 카운트)

#2 .upper() / .lower(): 대소문자 변경
word = "Hello Python"
print(word.upper())
print(len(word.upper()))

#3 .strip()
user_input = "  챗봇에게 질문할게요    "
print("1",len(user_input))
user_input = user_input.strip()
print("2",len(user_input))

#4 응용 .split()
sentence = "사과,바나나,포도"
print("split() 함수 연습")
fruits = sentence.split(",")
print(fruits)
print()
for i in fruits:
    print(i)

#5 응용 .replace()
review = "이 서비스는 별로예요"
fixed = review.replace("별로예", "괜찮아")
print(fixed)

#6 실무 f-string
user_name = "클라라"
question = "파이썬 딕셔너리 사용법"
# 실무 예시: 사용자 입력값을 넣어 AI에게 보낼 프롬프트를 자동 생성


#...리스트 부분
print()
# .index() / in
skills = ["Git", "Python", "OpenAI API"]
print("Python" in skills)
print(skills.index("Python"))
print()

# 리스트_컴프리헨션
# 실무 예시: AI API가 돌려준 답변 후보 리스트 중, 길이가 10자 이상인 것만 필터링

ai_responses = ["네", "안녕하세요! 무엇을 도와드릴까요?", "좋아요", "파이썬 학습을 시작해볼까요?"]

long_responses = [text for text in ai_responses if len(text) >= 10]

print(long_responses)
print()
# 딕셔너리
student = {"name": "클라라", "course": "AI서비스개발"}
print(student.keys())  # 출력: dict_keys(['name', 'course'])

print()

profile = {"이름": "클라라", "관심분야": "AI 서비스 기획"}
for key, value in profile.items():    
    print(f"{key}:{value}")
print()
#중첩 딕셔너리 다루기
# 실무 예시: OpenAI API 응답 형태를 흉내낸 딕셔너리
api_response = {    "id": "chatcmpl-123",   
                    "choices": [ { "message": { "role": "assistant",
                                                "content": "안녕하세요! 무엇을 도와드릴까요?"  } 
                     }  
                      ]
                } 
                    
# 서랍장(딕셔너리) 속 리스트, 그 리스트 속 딕셔너리를 차례로 열어서 답변만 꺼내기

answer = api_response["choices"][0]["message"]["content"]

print(answer)
print()
print(api_response.keys())
print()
print("choices 길이")
print(len(api_response["choices"]))
print()
print(api_response["choices"][0].keys())

myname = api_response["id"]
myanswer = api_response["choices"][0]