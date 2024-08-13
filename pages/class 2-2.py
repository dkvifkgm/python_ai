import streamlit as st

# number = st.number_input("請輸入一個數字", min_value=0, max_value=100)
# st.markdown(f"你輸入的數字是 {number}")

st.title("練習")
st.write("請輸入你的成績")
number = st.number_input("請輸入一個數字", min_value=0, max_value=100)
if number >= 100:
    st.markdown("你的等級是 A++")
elif number >= 95:
    st.markdown("你的等級是 A+")
elif number >= 90:
    st.markdown("你的等級是 A")
elif number >= 80:
    st.markdown("你的等級是 B")
elif number >= 70:
    st.markdown("你的等級是 C")
elif number >= 60:
    st.markdown("你的等級是 D")
elif number >= 50:
    st.markdown("你的等級是 E")
else:
    st.markdown("你的等級是 F")
