#=======================================
#  물류회사 AI 음성 챗봇 (Streamlit)
#
# 실행 : .venv\Scripts\python.exe -m streamlit run 5_lms_voice_test_app.py
#----------------------------------------

import io
import json
import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"

inventory = pd.read_csv(DATA_DIR / "logistics_inventory.csv")
deliveries = pd.read_csv(DATA_DIR / "logistics_deliveries.csv")
accidents = pd.read_csv(DATA_DIR / "logistics_accidents.csv")


# --------------------------------------------------
# 물류 데이터 도구
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
    return "물류 사고 보고서를 작성했습니다.\n" + "\n".join(lines)


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
            "properties": {
                function.__code__.co_varnames[0]: {"type": "string"}
            },
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
OPENAI_MODEL = "gpt-4.1-mini"


def get_client():
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")
    try:
        from openai import OpenAI
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "openai 패키지가 없습니다. '.venv\\Scripts\\python.exe -m pip install openai'를 실행하세요."
        ) from error
    return OpenAI(api_key=api_key)


def ask(question: str) -> str:
    """질문에 맞는 물류 도구를 실행하고 최종 답변을 반환한다."""
    client = get_client()
    messages = [{"role": "user", "content": question}]
    response = client.responses.create(
        model=OPENAI_MODEL,
        input=messages,
        tools=TOOLS,
        temperature=0,
    )

    function_calls = [
        item for item in response.output if item.type == "function_call"
    ]
    if not function_calls:
        return response.output_text

    messages += response.output
    for call in function_calls:
        result = FUNCTIONS[call.name](**json.loads(call.arguments))
        messages.append(
            {
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": result,
            }
        )

    final = client.responses.create(model=OPENAI_MODEL, input=messages)
    return final.output_text


def transcribe_audio(audio_file) -> str:
    """Streamlit 업로드 음성 파일을 Whisper로 텍스트 변환한다."""
    client = get_client()
    audio = io.BytesIO(audio_file.getvalue())
    audio.name = audio_file.name
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio,
    )
    return transcript.text


# --------------------------------------------------
# Streamlit 화면
# --------------------------------------------------
st.set_page_config(page_title="LogiDesk 운영 관제", page_icon="🚚", layout="wide")
st.markdown(
    """
    <style>
    .stApp { background: #f4f6f8; }
    [data-testid="stSidebar"] { background: #17212b; }
    [data-testid="stSidebar"] * { color: #e9eef2; }
    .brand { color: #0d6b6f; font-size: 2rem; font-weight: 800; letter-spacing: -0.04em; }
    .eyebrow { color: #687782; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; }
    .status { color: #237a4b; font-size: 0.85rem; font-weight: 700; }
    div[data-testid="stMetric"] { background: white; border: 1px solid #dfe5e9; border-radius: 8px; padding: 14px 16px; }
    div[data-testid="stChatMessage"] { border: 1px solid #e1e7ea; border-radius: 8px; background: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🚚 LogiDesk")
    st.caption("물류 운영 통합 관제")
    st.divider()
    st.markdown("**운영 메뉴**")
    st.radio("화면", ["AI 운영 오퍼레이터", "재고 현황", "배송 모니터링", "사고 관리"], label_visibility="collapsed")
    st.divider()
    st.markdown("**시스템 상태**")
    st.markdown("🟢 데이터 연결 정상")
    st.markdown("🟢 AI 오퍼레이터 대기 중")
    st.caption("최종 동기화: 방금 전")

st.markdown('<div class="eyebrow">Operations Control Center</div>', unsafe_allow_html=True)
st.markdown('<div class="brand">물류 운영 관제</div>', unsafe_allow_html=True)
st.markdown('<span class="status">● 실시간 운영 상태 정상</span>', unsafe_allow_html=True)

low_stock_count = int((inventory["stock"] <= 20).sum())
delay_count = int(
    deliveries[
        (deliveries["week"] == "이번주") & (deliveries["status"] == "지연")
    ]["count"].sum()
)
accident_count = len(accidents)
center_count = inventory["center"].nunique()

metric_columns = st.columns(4)
metric_columns[0].metric("관리 센터", f"{center_count}곳", "운영 중")
metric_columns[1].metric("재고 부족 품목", f"{low_stock_count}건", "20개 이하")
metric_columns[2].metric("이번 주 배송 지연", f"{delay_count}건", "전 지역 합계")
metric_columns[3].metric("누적 사고 접수", f"{accident_count}건", "데이터 기준")

st.divider()

EXAMPLE_QUESTIONS = [
    "강남센터 재고 부족 상품 알려줘",
    "부산 배송 지연 건수는?",
    "파손 사고 내용을 보고서로 만들어줘",
]

if "messages" not in st.session_state:
    st.session_state.messages = []
if "input_box" not in st.session_state:
    st.session_state.input_box = ""


def fill_example(question: str) -> None:
    st.session_state.input_box = question


st.subheader("질문 예시")
example_columns = st.columns(len(EXAMPLE_QUESTIONS))
for column, question in zip(example_columns, EXAMPLE_QUESTIONS):
    column.button(
        question,
        use_container_width=True,
        on_click=fill_example,
        args=(question,),
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


st.subheader("음성으로 질문하기")
uploaded_audio = st.file_uploader(
    "음성 파일을 선택하세요.",
    type=["mp3", "wav", "m4a", "webm", "mp4", "mpeg", "mpga"],
)
if uploaded_audio:
    st.audio(uploaded_audio)
    if st.button("음성 인식 후 질문하기", type="primary", use_container_width=True):
        try:
            with st.spinner("음성을 인식하고 답변을 만드는 중입니다..."):
                question = transcribe_audio(uploaded_audio)
                answer = ask(question)
            st.session_state.messages.extend(
                [
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer},
                ]
            )
            st.rerun()
        except Exception as error:
            st.error(f"음성 질문을 처리하지 못했습니다: {error}")


def submit_question() -> None:
    question = st.session_state.input_box.strip()
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    try:
        with st.spinner("답변을 만드는 중입니다..."):
            answer = ask(question)
    except Exception as error:
        answer = f"요청을 처리하지 못했습니다: {error}"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.input_box = ""


with st.form(key="question_form", clear_on_submit=False):
    st.text_input("메시지를 입력하세요.", key="input_box")
    st.form_submit_button("전송", on_click=submit_question, type="primary")
