import streamlit as st
import random
from utils import set_background

number = st.number_input("請輸入一個數字", min_value=0, max_value=100)
st.markdown(f"你輸入的數字是 {number}")

st.markdown("---")

st.title("練習")
score = st.number_input("請輸入你的成績", min_value=0, max_value=100)
if score >= 95:
    st.markdown("你的等級是 A+")
elif score >= 90:
    st.markdown("你的等級是 A")
elif score >= 80:
    st.markdown("你的等級是 B")
elif score >= 70:
    st.markdown("你的等級是 C")
elif score >= 60:
    st.markdown("你的等級是 D")
elif score >= 50:
    st.markdown("你的等級是 E")
else:
    st.markdown("你的等級是 F")

st.markdown("---")

st.markdown("按鈕練習")
if st.button("按我一下"):
    random.randint(1, 3)
    if random.randint(1, 3) == 1:
        set_background("image/bg.png", width=20, position="left bottom")
    elif random.randint(1, 3) == 2:
        set_background("image/bg.png", width=20, position="center bottom")
    else:
        set_background("image/bg.png", width=20, position="right bottom")
