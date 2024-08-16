import streamlit as st
import openai  # pip install openai
from utils import load_openai_api

openai.api_key = load_openai_api()  # 載入openai api 的金鑰

if "history" not in st.session_state:  # 初始化對話紀錄
    st.session_state.history = []  # 對話紀錄

if "system_message" not in st.session_state:
    st.session_state.system_message = "你只能使用英文跟繁體中文"  # 系統訊息

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"  # 系統訊息

col1, col2, col3 = st.columns([4, 2, 1])  # 分割兩個列
with col1:
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )
with col2:
    st.session_state.model = st.selectbox("模型", ["gpt-4o-2024-08-06", "gpt-4o-mini"])


with col3:
    if st.button("清除對話紀錄"):
        st.session_state.history = []  # 清空對話紀錄
        st.rerun()  # 重新整理頁面

for message in st.session_state.history:  # 透過對話紀錄來初始化對話紀錄列表
    if message["role"] == "user":  # 如果是用戶訊息
        st.chat_message("user", avatar="🙂").write(message["content"])  # 顯示用戶訊息
    else:  # 如果是AI訊息
        st.chat_message("assistant", avatar="👽").write(
            message["content"]
        )  # 顯示AI訊息

prompt = st.chat_input("請輸入想要對話的訊息")
if prompt:  # 如果有輸入訊息
    st.session_state.history.append(
        {"role": "user", "content": prompt}
    )  # 將用戶訊息加入對話紀錄
    responce = openai.chat.completions.create(
        model=st.session_state.model,  # 設定ai的模型
        temperature=0.1,  # 溫度參數 設定回答的創意性 值越大變化越大
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )

    assistant_massage = responce.choices[0].message.content  # 取得ai回傳的訊息
    st.session_state.history.append(
        {"role": "assistant", "content": assistant_massage}
    )  # 將AI訊息加入對話紀錄
    st.rerun()  # 重新整理頁面
