#=======================================
#  AI 배차 추천 시스템 예제
#
# 실행 : streamlit run 6_dispatch_recommend_app.py
#----------------------------------------


import json
import pandas as pd

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# 프로젝트 루트
cargos = pd.read_csv("./data/dms_cargos.csv")
drivers = pd.read_csv("./data/dms_drivers.csv")


# --------------------------------------------------
# 배차 추천 점수 산정 (출발지 / 화물유형 / 톤수 / 평점)
# --------------------------------------------------
def _rating_score(rating: float):
    """평점을 점수와 설명 라벨로 변환한다."""
    if rating >= 4.5:
        return 20, "우수"
    if rating >= 4.0:
        return 15, "양호"
    if rating >= 3.5:
        return 10, "보통"
    return 5, "낮음"


def _tonnage_score(vehicle_ton: float, weight_ton: float):
    """차량 톤수가 화물 톤수를 감당할 수 있는지, 얼마나 적합한지 점수화한다."""
    if vehicle_ton < weight_ton:
        return 0
    excess = vehicle_ton - weight_ton
    if excess <= 3:
        return 25
    if excess <= 6:
        return 18
    return 10


def _score_driver(cargo, driver):
    """화물 한 건에 대해 차주 한 명의 적합도 점수(0~100)와 추천 사유를 계산한다."""
    score = 0
    reasons = []

    # ① 출발지 일치 (25점)
    if driver["base_region"] == cargo["origin"]:
        score += 25
        reasons.append(f"출발지가 {cargo['origin']}으로 동일")
    else:
        reasons.append(f"출발지 불일치 ({driver['base_region']} ≠ {cargo['origin']})")

    # ② 화물 유형 운송 가능 여부 (25점)
    capabilities = [c.strip() for c in str(driver["capabilities"]).split(",")]
    if cargo["cargo_type"] in capabilities:
        score += 25
        reasons.append(f"{cargo['cargo_type']} 운송 가능")
    else:
        reasons.append(f"{cargo['cargo_type']} 운송 불가")

    # ③ 톤수 적합성 (25점)
    tonnage_pts = _tonnage_score(driver["vehicle_ton"], cargo["weight_ton"])
    score += tonnage_pts
    if driver["vehicle_ton"] >= cargo["weight_ton"]:
        reasons.append(f"{int(cargo['weight_ton'])}톤 화물에 적합한 {int(driver['vehicle_ton'])}톤 차량")
    else:
        reasons.append(f"{int(driver['vehicle_ton'])}톤 차량으로 {int(cargo['weight_ton'])}톤 화물 운송 불가")

    # ④ 평점 (20점)
    rating_pts, rating_label = _rating_score(driver["rating"])
    score += rating_pts
    reasons.append(f"평점 {driver['rating']}로 {rating_label}")

    return score, reasons


# --------------------------------------------------
# 실제 함수
# --------------------------------------------------
def recommend_driver(order_id: str) -> str:
    """화물 주문번호(예: ORD-001)를 받아 가장 적합한 차주를 추천한다. 출발지, 화물유형, 톤수, 평점을 점수화해 1위 차주와 추천 사유, 점수를 반환한다. 배차/추천 질문에 사용."""
    cargo_row = cargos[cargos["order_id"] == order_id]
    if cargo_row.empty:
        return f"주문번호 {order_id}를 찾지 못했습니다."
    cargo = cargo_row.iloc[0]

    available = drivers[drivers["status"] == "가능"]
    if available.empty:
        return "현재 가동 가능한 차주가 없습니다."

    ranked = sorted(
        (_score_driver(cargo, d) + (d,) for _, d in available.iterrows()),
        key=lambda x: x[0],
        reverse=True,
    )
    best_score, best_reasons, best_driver = ranked[0]

    numbering = ["①", "②", "③", "④", "⑤", "⑥"]
    reason_lines = "\n".join(f"{numbering[i]} {r}" for i, r in enumerate(best_reasons))

    return (
        "🚚 AI 배차 추천\n\n"
        f"추천 차주: {best_driver['name']} ({best_driver['driver_id']})\n\n"
        "추천 이유\n"
        f"{reason_lines}\n\n"
        f"추천 점수: {best_score}점"
    )


def get_cargo_info(order_id: str) -> str:
    """화물 주문번호를 받아 출발지/도착지/화물종류/중량/상태를 반환한다. 화물 상세 조회에 사용."""
    row = cargos[cargos["order_id"] == order_id]
    if row.empty:
        return f"주문번호 {order_id}를 찾지 못했습니다."
    r = row.iloc[0]
    return (
        f"{order_id}: {r['origin']} → {r['destination']}, "
        f"{r['cargo_type']} {int(r['weight_ton'])}톤, 상태={r['status']}"
    )


def list_available_drivers(region: str) -> str:
    """지역명을 받아 해당 지역 소속이면서 현재 가동 가능한 차주 목록을 반환한다. '어떤 차주 있어?' 류 질문에 사용."""
    hit = drivers[(drivers["base_region"] == region) & (drivers["status"] == "가능")]
    if hit.empty:
        return f"{region} 지역에 가동 가능한 차주가 없습니다."
    names = [f"{r['name']}({r['driver_id']})" for _, r in hit.iterrows()]
    return f"{region} 가동 가능 차주: " + ", ".join(names)


# --------------------------------------------------
# 함수 등록
# --------------------------------------------------
FUNCTIONS = {
    "recommend_driver": recommend_driver,
    "get_cargo_info": get_cargo_info,
    "list_available_drivers": list_available_drivers,
}

# recommend_driver는 서식이 고정된 결과를 반환하므로, 2차 LLM 응답 생성 없이 결과를 그대로 사용자에게 전달한다.
DIRECT_RETURN_FUNCTIONS = {"recommend_driver"}


# --------------------------------------------------
# Tool 스키마 자동 생성
# --------------------------------------------------
TOOLS = [
    {
        "type": "function",
        "name": name,
        "description": func.__doc__ or "",
        "parameters": {
            "type": "object",
            "properties": {
                list(func.__code__.co_varnames[:func.__code__.co_argcount])[0]: {
                    "type": "string"
                }
            },
            "required": [
                list(func.__code__.co_varnames[:func.__code__.co_argcount])[0]
            ],
        },
    }
    for name, func in FUNCTIONS.items()
]

# ============================
# OpenAI API를 사용
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
OPENAI_MODEL = "gpt-4.1-mini"


# --------------------------------------------------
# 질문 함수
# --------------------------------------------------
def ask(question):
    """질문을 받아 모델이 알맞은 도구를 골라 실행하고(자동), 최종 답변을 돌려준다."""

    #=================================================
    #  OpenAI API를 사용하여 응답 생성
    messages = [{"role": "user", "content": question}]

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=messages,
        tools=TOOLS,
        temperature=0,
    )
    #================================================

    function_calls = [item for item in response.output if item.type == "function_call"]

    if not function_calls:
        return response.output_text

    messages += response.output

    tool_results = {}
    for call in function_calls:
        result = FUNCTIONS[call.name](
            **json.loads(call.arguments)
        )
        tool_results[call.name] = result

        messages.append({
            "type": "function_call_output",
            "call_id": call.call_id,
            "output": result,
        })

    if any(name in DIRECT_RETURN_FUNCTIONS for name in tool_results):
        return "\n\n".join(tool_results[name] for name in tool_results if name in DIRECT_RETURN_FUNCTIONS)

    final = client.responses.create(
        model=OPENAI_MODEL,
        input=messages,
    )

    return final.output_text


# --------------------------------------------------
# 화면 (Streamlit)
# --------------------------------------------------
st.set_page_config(page_title="AI 배차 추천", page_icon="🚚")
st.title("🚚 AI 배차 추천 시스템")

EXAMPLE_QUESTIONS = [
    "ORD-001 화물에 가장 적합한 차주를 추천해줘.",
    "ORD-003 화물 상태 알려줘.",
    "인천에 가동 가능한 차주 있어?",
    "ORD-007 화물 배차 추천해줘.",
]

st.caption("질문 예시")
example_cols = st.columns(len(EXAMPLE_QUESTIONS))
clicked_question = None
for col, q in zip(example_cols, EXAMPLE_QUESTIONS):
    if col.button(q, use_container_width=True):
        clicked_question = q

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

chat_input = st.chat_input("메시지를 입력하세요.")
user_input = clicked_question or chat_input

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    answer = ask(user_input)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)