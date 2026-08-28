#=======================================
#  우리회사 전용 간단한 챗봇 예제
# 
# 실행 : streamlit run 3_chatbot_mycom_app.py
#----------------------------------------


import json
import pandas as pd

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


# 프로젝트 루트
products = pd.read_csv( "./data/pms_products.csv")
inventory = pd.read_csv("./data/pms_inventory.csv")
orders = pd.read_csv("./data/pms_orders.csv")


# --------------------------------------------------
# 실제 함수
# --------------------------------------------------
def get_price(product_name: str) -> str:
    """상품명(일부만 입력해도 됨)을 받아 판매가(원)를 반환한다. 가격/얼마 질문에 사용."""
    row = products[products["product_name"].str.contains(product_name, na=False)]
    if row.empty:
        return f"'{product_name}' 가격 정보를 찾지 못했습니다."
    r = row.iloc[0]
    return f"{r['product_name']} 판매가 {int(r['price']):,}원"

def get_stock(product_name: str) -> str:
    """상품명(일부만 입력해도 됨)을 받아 현재 재고 수량과 창고를 반환한다. 재고/품절 질문에 사용."""
    row = inventory[inventory["product_name"].str.contains(product_name, na=False)]
    if row.empty:
        return f"'{product_name}' 재고 정보를 찾지 못했습니다."
    r = row.iloc[0]
    return f"{r['product_name']} 재고 {int(r['stock'])}개 ({r['warehouse']})"

def get_order_status(order_id: str) -> str:
    """주문번호(예: O000106)를 받아 배송 상태를 반환한다. 주문/배송 추적에 사용."""
    row = orders[orders["order_id"] == order_id]
    if row.empty:
        return f"주문번호 {order_id}를 찾지 못했습니다."
    r = row.iloc[0]
    return f"주문 {order_id}: {r['product_name']} {int(r['quantity'])}개, 상태={r['status']}"

def search_product(keyword: str) -> str:
    """카테고리나 키워드로 상품을 검색해 이름 목록을 반환한다. '어떤 상품 있어?' 류에 사용."""
    hit = products[products["product_name"].str.contains(keyword, na=False) |
                   products["category"].str.contains(keyword, na=False)]
    if hit.empty:
        return f"'{keyword}' 관련 상품이 없습니다."
    return "검색 결과: " + ", ".join(hit["product_name"].head(5).tolist())



# --------------------------------------------------
# 함수 등록
# --------------------------------------------------
FUNCTIONS = {
    "get_price": get_price,
    "get_stock": get_stock,
    "get_order_status": get_order_status,
    "search_product": search_product,
}


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

    #==================================================
    # OpenAI API를 사용하여 응답 생성
    
    messages = [{"role": "user", "content": question}]

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=messages,
        tools=TOOLS,
        temperature=0,
    )
    #=================================================

    function_calls = [item for item in response.output if item.type == "function_call"]

    if not function_calls:
        return response.output_text

    messages += response.output

    for call in function_calls:
        result = FUNCTIONS[call.name](
            **json.loads(call.arguments)
        )

        messages.append({
            "type": "function_call_output",
            "call_id": call.call_id,
            "output": result,
        })

    final = client.responses.create(
        model=OPENAI_MODEL,
        input=messages,
    )

    return final.output_text


# --------------------------------------------------
# 화면 (Streamlit)
# --------------------------------------------------
st.set_page_config(page_title="쇼핑몰 챗봇", page_icon="🛒")
st.title("🛒 쇼핑몰 챗봇")

EXAMPLE_QUESTIONS = [
    "슬림핏 청바지 얼마야?",
    "이어버드 재고 있어?",
    "주문 O000106 배송 어디까지 왔어?",
    "패션의류 상품 보여줘",
]

if "messages" not in st.session_state:
    st.session_state.messages = []
if "input_box" not in st.session_state:
    st.session_state.input_box = ""

def _fill_example(question):
    st.session_state.input_box = question

st.caption("질문 예시 (클릭하면 입력창에 채워집니다)")
example_cols = st.columns(len(EXAMPLE_QUESTIONS))
for col, q in zip(example_cols, EXAMPLE_QUESTIONS):
    col.button(q, use_container_width=True, on_click=_fill_example, args=(q,))

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def _submit():
    question = st.session_state.input_box
    if not question:
        return
    st.session_state.messages.append({"role": "user", "content": question})
    answer = ask(question)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.input_box = ""

with st.form(key="question_form"):
    st.text_input("메시지를 입력하세요.", key="input_box")
    st.form_submit_button("전송", on_click=_submit)

