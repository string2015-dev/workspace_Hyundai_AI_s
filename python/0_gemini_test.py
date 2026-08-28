import os

from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("Gemini_API_KEY")
if not api_key:
    raise RuntimeError(".env에 Gemini_API_KEY를 설정하세요.")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="너는 누구야?",
)

print(response.text)