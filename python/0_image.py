from openai import OpenAI
import base64
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.images.generate(
    model="gpt-image-1",          # DALL-E 3를 쓰고 싶으면 "dall-e-3"로 변경
    prompt="샤워 머리 핀을 꽂은 채, 배달로 시킨 엽기떡볶이를 먹고 있는 사복차림 쥐.",
    size="1024x1024",             # 필요에 따라 "1792x1024"(가로), "1024x1792"(세로) 등으로 변경 가능
    n=1,
)

# gpt-image-1은 base64로 이미지를 반환하므로 파일로 저장
image_base64 = response.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

output_path = "generated_image.png"
with open(output_path, "wb") as f:
    f.write(image_bytes)

print(f"이미지 저장 완료: {output_path}")