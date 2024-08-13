import streamlit as st

number = st.number_input("請輸入一個數字", min_value=0, max_value=100)
st.markdown(f"你輸入的數字是 {number}")

st.markdown("---")

st.title("練習")
st.write("請輸入你的成績")
score = st.number_input("請輸入一個數字", min_value=0, max_value=100)
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

st.title("按鈕練習")
st.buttle("按我一下,key=1")
st.buttle("按我二下,key=2")

st.markdown("---")
