import streamlit as st

#
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

# 多個column
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{1+1}", key=f"{i+10}")

st.markdown("---")

st.title("文字輸入元件")
text = st.text_input("輸入文字", value="這是預設文字")
st.markdown(f"文字輸入的值為: {text}")

st.markdown("---")

st.title("columns 排列元件效果比較")
col1, col2, col3 = st.columns(3)
with col1:
    st.button("按鈕1", key="1")
    st.button("按鈕2", key="2")
    st.button("按鈕3", key="3")
with col2:
    st.write("這是col1")
    st.write("這是col2")
    st.write("這是col3")

st.markdown("---")

for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"{i+4}")
    with col2:
        st.write(f"這是col2")

st.markdown("---")

st.title("session_state")
ans = 1
if st.button("按下去ans+1", key="ans"):
    ans = ans + 1
st.write(f"ans = {ans}")  # 顯示結果

if "ans" not in st.session_state:  # 如果session_state中沒有ans這個變數
    st.session_state.ans = 1  # 設定session_state中的ans為1

st.rerun  # \強制重新整理
if st.button("重新整理畫面", key="banans"):  # 如果按下按鈕
    st.rerun()  # 重新執行程式
