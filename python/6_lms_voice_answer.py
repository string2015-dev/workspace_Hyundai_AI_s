#=======================================
#  물류회사 AI 음성 질의응답 데모
#
# 실행 : python 6_lms_voice_answer.py
#----------------------------------------

import glob
import json
import os
import sys
from pathlib import Path

import pandas as pd
import pygame
from dotenv import load_dotenv
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")


# 프로젝트 루트
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
ANSWER_DIR = PROJECT_ROOT / "answers"

inventory = pd.read_csv(DATA_DIR / "logistics_inventory.csv")
deliveries = pd.read_csv(DATA_DIR / "logistics_deliveries.csv")
accidents = pd.read_csv(DATA_DIR / "logistics_accidents.csv")


# --------------------------------------------------
# 실제 함수
# --------------------------------------------------
def get_low_stock(center: str) -> str:
    """물류센터명(예: 강남센터)을 받아 재고 20개 이하인 재고 부족 상품 목록을 반환한다. 재고 부족 질문에 사용."""
    row = inventory[(inventory["center"] == center) & (inventory["stock"] <= 20)]
    if row.empty:
        return f"'{center}'에는 재고 부족 상품이 없습니다."
    names = ", ".join(row["product_name"].tolist())
    return f"현재 재고가 20개 이하인 상품은 {names}입니다."


def get_delivery_delay_count(region: str) -> str:
    """지역명(예: 부산)을 받아 이번 주 배송 지연 건수를 반환한다. 배송 지연 질문에 사용."""
    row = deliveries[
        (deliveries["region"] == region)
        & (deliveries["week"] == "이번주")
        & (deliveries["status"] == "지연")
    ]
    if row.empty:
        return f"'{region}' 지역의 이번 주 배송 지연 데이터가 없습니다."
    count = int(row["count"].sum())
    return f"이번 주 {region} 지역 배송 지연은 {count}건입니다."


def generate_accident_report(keyword: str) -> str:
    """사고 유형 키워드(예: 파손, 분실, 오배송)를 받아 해당 사고들을 정리한 보고서를 작성한다. 사고 보고서 작성 요청에 사용."""
    row = accidents[accidents["type"].str.contains(keyword, na=False)]
    if row.empty:
        return f"'{keyword}' 관련 사고 이력이 없습니다."

    total_qty = int(row["quantity"].sum())
    lines = [f"[{keyword} 사고 보고서] 총 {len(row)}건, 수량 {total_qty}개"]
    for _, accident in row.iterrows():
        lines.append(
            f"- {accident['date']} {accident['product_name']} "
            f"{int(accident['quantity'])}개: {accident['description']}"
        )
    return f"물류 사고 보고서를 작성했습니다.\n{chr(10).join(lines)}"


FUNCTIONS = {
    "get_low_stock": get_low_stock,
    "get_delivery_delay_count": get_delivery_delay_count,
    "generate_accident_report": generate_accident_report,
}

TOOLS = [
    {
        "type": "function",
        "name": name,
        "description": function.__doc__ or "",
        "parameters": {
            "type": "object",
            "properties": {function.__code__.co_varnames[0]: {"type": "string"}},
            "required": [function.__code__.co_varnames[0]],
        },
    }
    for name, function in FUNCTIONS.items()
]


# --------------------------------------------------
# OpenAI API
# --------------------------------------------------
load_dotenv(PROJECT_ROOT / ".env")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")

client = OpenAI(api_key=api_key)
OPENAI_MODEL = "gpt-4.1-mini"
TTS_MODEL = "gpt-4o-mini-tts"
TTS_VOICE = "coral"


def ask(question: str) -> str:
    """질문에 맞는 물류 도구를 실행하고 최종 답변을 반환한다."""
    messages = [{"role": "user", "content": question}]
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=messages,
        tools=TOOLS,
        temperature=0,
    )

    function_calls = [item for item in response.output if item.type == "function_call"]
    if not function_calls:
        return response.output_text

    messages += response.output
    for call in function_calls:
        result = FUNCTIONS[call.name](**json.loads(call.arguments))
        messages.append(
            {"type": "function_call_output", "call_id": call.call_id, "output": result}
        )

    final = client.responses.create(model=OPENAI_MODEL, input=messages)
    return final.output_text


def transcribe_audio(file_path: str) -> str:
    """mp3 등 음성 파일을 텍스트로 변환한다."""
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
    return transcript.text


def synthesize_speech(text: str, output_path: Path) -> None:
    """텍스트 답변을 MP3 음성 파일로 저장한다."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with client.audio.speech.with_streaming_response.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text,
        response_format="mp3",
    ) as response:
        response.stream_to_file(output_path)


def play_audio(file_path: Path) -> None:
    """파이썬 프로세스 안에서 MP3를 재생한다."""
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    print("물류 AI 음성 질의응답을 시작합니다.")
    print("음성 파일을 찾을 수 없으면 종료됩니다.")

    for audio_path in sorted(glob.glob(str(DATA_DIR / "*.mp3"))):
        question = transcribe_audio(audio_path)
        answer = ask(question)
        answer_path = ANSWER_DIR / f"{Path(audio_path).stem}_answer.mp3"
        synthesize_speech(answer, answer_path)

        print(f"음성 파일: {audio_path}")
        print(f"인식된 질문: {question}")
        print(f"텍스트 답변: {answer}")
        print(f"음성 답변: {answer_path}")
        play_audio(answer_path)
        print("-" * 40)