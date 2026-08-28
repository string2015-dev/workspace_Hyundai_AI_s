#=======================================
#  물류회사 AI 데모 (Streamlit)
#
# 실행 : streamlit run 4_Ims_test_app.py
#----------------------------------------

import json
import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# 앱 파일의 위치를 기준으로 데이터 파일을 읽어 실행 위치와 무관하게 동작시킨다.
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"

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
    report = "\n".join(lines)
    return f"물류 사고 보고서를 작성했습니다.\n{report}"


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


def ask(question: str) -> str:
    """질문에 맞는 물류 도구를 실행하고 최종 답변을 반환한다."""
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY가 설정되지 않았습니다. .env 파일을 확인하세요.")

    client = OpenAI(api_key=api_key)
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


# --------------------------------------------------
# Streamlit 화면
# --------------------------------------------------
st.set_page_config(page_title="물류회사 AI", page_icon="🚚")
st.title("🚚 물류회사 AI 데모")
st.caption("물류 데이터를 바탕으로 재고, 배송 지연, 사고 보고서를 조회합니다.")

with st.expander("물류 AI 처리 흐름", expanded=True):
    st.code(
        "물류 데이터 → AI가 질문 분석 → 재고조회 / 배송조회 / 사고보고 → 답변",
        language="text",
    )

EXAMPLE_QUESTIONS = [
    "부산센터 재고 부족 상품 알려줘",
    "인천 배송 지연 건수는?",
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


def submit_question() -> None:
    question = st.session_state.input_box.strip()
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    try:
        answer = ask(question)
    except Exception as error:
        answer = f"요청을 처리하지 못했습니다: {error}"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.input_box = ""


with st.form(key="question_form", clear_on_submit=False):
    st.text_input("메시지를 입력하세요.", key="input_box")
    st.form_submit_button("전송", on_click=submit_question)