import os

from dotenv import load_dotenv
from google import genai


# .env 파일의 환경 변수를 불러옵니다.
load_dotenv()

# Client 생성 (GEMINI_API_KEY 환경 변수를 자동으로 탐색하여 적용)
client = genai.Client()

# Gemini 모델 호출
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="너는 누구야?",
)

print(response.text)