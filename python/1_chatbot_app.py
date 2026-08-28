#=======================================
# 간단한 챗봇 예제
# 
# 실행 : streamlit run 1_chatbot_app.py
#----------------------------------------

import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="챗봇", page_icon="🤖")
st.title("🤖 간단한 챗봇")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("메시지를 입력하세요.")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # =====================================
    # OpenAI API를 사용하여 응답 생성
    # [ 여기에 코드를 작성합니다 ]
    respone = client.responses.create(
        model="gpt-4.1-mini",
        input=st.session_state.messages
    )
    answer = respone.output_text

    # =====================================

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
