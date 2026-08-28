#=======================================
#  물류회사 AI 데모 ( 보여주기용 예제)
#
# 실행 : python test.py
#----------------------------------------

import json
import sys
import pandas as pd

import os
from dotenv import load_dotenv
from openai import OpenAI

sys.stdout.reconfigure(encoding="utf-8")


# 프로젝트 루트
inventory = pd.read_csv("./data/logistics_inventory.csv")
deliveries = pd.read_csv("./data/logistics_deliveries.csv")
accidents = pd.read_csv("./data/logistics_accidents.csv")


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
    for _, r in row.iterrows():
        lines.append(
            f"- {r['date']} {r['product_name']} {int(r['quantity'])}개: {r['description']}"
        )
    report = "\n".join(lines)
    return f"물류 사고 보고서를 작성했습니다.\n{report}"


# --------------------------------------------------
# 함수 등록
# --------------------------------------------------
FUNCTIONS = {
    "get_low_stock": get_low_stock,
    "get_delivery_delay_count": get_delivery_delay_count,
    "generate_accident_report": generate_accident_report,
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

    # =================================================
    #  OpenAI API를 사용하여 응답 생성
    # [ 여기에 코드를 작성하거나 복사하세요 ]
   
    messages = [{"role": "user", "content": question}] #사용자 질문을 사용자 메세지로 사용할거야.
    response = client.responses.create(
           model=OPENAI_MODEL,
           input=messages,
           tools=TOOLS, #앞서 각 정보를 검색하는 건 AI아님. 검색한 정보를 가지고 배송정보인지, 재고정보인지 확인하는건 AI가 하는거야. 그래서 tools=TOOLS를 넣어줘야해.
           temperature=0
    )


    # =================================================

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
# 데모 소개 (물류 AI 흐름도)
# --------------------------------------------------
BANNER = """
        물류 데이터 
           ↓
    ┌─────────────┐
    │     AI      │
    └─────────────┘
    ↓     ↓     ↓
 재고조회 배송조회 사고보고
    ↓     ↓     ↓
 "127개" "내일 도착" "파손 10개"
""" # 물류 데이터 부분에 사용자가 질문을 하면 AI가 적절한 도구(재고조회, 배송조회, 사고보고)를 선택하여 실행하고 최종 답변을 돌려주는 흐름을 보여줌.
    # 프로그램을 짤지 인공지능을 사용할지 선택하는 것이 아니라, 인공지능이 적절한 도구를 선택하여 실행하고 최종 답변을 돌려주는 흐름을 보여줌.


# --------------------------------------------------
# 테스트 (콘솔 확인용)
# --------------------------------------------------
if __name__ == "__main__":
    print(BANNER)

    for q in [
        "부산센터 재고 부족 상품 알려줘",
        "인천 배송 지연 건수는?",
        "파손 사고 내용을 보고서로 만들어줘",
    ]:
        print(f"👤 {q}")
        print(f"🤖 {ask(q)}")
        print("-" * 40)
