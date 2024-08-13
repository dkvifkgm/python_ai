import streamlit as st

st.markdown("數字金字塔")
pymrid = st.number_input("請輸入一個數字", min_value=1, max_value=9)
for i in range(1, pymrid + 1):
    st.markdown(f"{i}" * i)
