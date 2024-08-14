import streamlit as st

st.title("點餐機")
if "L" not in st.session_state:  # 如果session_state中沒有L這個變數
    st.session_state.L = []  # 設定session_state中的L為空陣列

columns = st.columns(2)
with columns[0]:
    food = st.text_input("請輸入餐點")
with columns[1]:
    if st.button("加入餐點"):
        st.session_state.L.append(food)  # 將餐點加入陣列中並存入session_state
st.title("購物籃")
for i in range(len(st.session_state.L)):  # 逐一印出陣列中的元素
    columns = st.columns(2)
    with columns[0]:
        st.write(st.session_state.L[i])  # 將陣列中的指定位置的元素印出來
    with columns[1]:
        if st.button("刪除", key=i):
            st.session_state.L.pop(i)  # 刪除陣列中的指定位置的元素並存入session_state
            st.rerun()  # 重新執行程式
