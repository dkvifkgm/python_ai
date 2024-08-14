import streamlit as st

# column 排版
st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1", key="1")
col2.button("按鈕2", key="2")

col1, col2 = st.columns([1, 2])  # 可自由設定比例
col1.button("按鈕1", key="3")
col2.button("按鈕2", key="4")

col1, col2, col3 = st.columns([1, 2, 1])
col1.button("按鈕1", key="5")
col2.button("按鈕2", key="6")
col3.button("按鈕3", key="7")

# with col1: st.button 的意思跟 col1.button 一樣
with col1:
    st.button("按鈕1", key="8")
    st.button("按鈕2", key="9")
