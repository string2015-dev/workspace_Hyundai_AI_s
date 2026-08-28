from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-5.6", 
    input="너는 누구야?" # 보기 편하게 들여쓰기
)

print(response.output_text) # 설치 끝나고 돌려봅시다