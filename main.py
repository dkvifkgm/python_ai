import streamlit as st
from utils import set_background  # 從utils只匯入set_background函數

st.title("歡迎使用Streamlit")

set_background("image/bg.png", width=20, position="left bottom")
