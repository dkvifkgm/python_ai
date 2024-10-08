import streamlit as st

st.title("數字金字塔")
pymrid = st.number_input("請輸入一個數字", min_value=1, max_value=100)
for i in range(1, pymrid + 1):
    st.markdown(f"{i}" * i)

st.markdown("---")

st.markdown("箭頭金字塔")
n = st.number_input("請輸入一個整數", min_value=1, step=1)
arrow = ""
for i in range(1, n + 1):
    arrow = arrow + (" " * (n - i) + "*" * (2 * i - 1) + "\n")
for i in range(n):
    arrow = arrow + (" " * (n - 1) + "*" + "\n")

st.markdown(f"```\n . \n{arrow}\n```")
