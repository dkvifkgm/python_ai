import streamlit as st
import os
import time

image_folder = "image"  # 資料夾的內容存入變數image_folder
image_files = os.listdir(image_folder)

if "products" not in st.session_state:  # 如果session_state中沒有products這個變數
    st.session_state.products = {}  # 建立products的session_state

for image_file in image_files:  # 將圖片名稱存入products
    products_name = image_file[:-4]  # 去掉副檔名
    if products_name not in st.session_state.products:
        st.session_state.products[products_name] = {"price": 10, "stock": 10, "image":  f"{image_folder}/{image_file}"}

#顯示商品
st.title("購物平台")
col_number = st.number_input("請輸入商品欄數", min_value=1, max_value=10, step=1)
cols = st.columns(col_number) #分成兩欄顯示商品

i = 0 
for product_name,details in st.session_state.products.items(): #逐一顯示商品
    #producte_name是商品名稱，details是商品的詳細資料和資訊(價格、庫存、圖片)
    with cols[i%len(cols)]:#透過取餘數決定商品要顯示在哪一欄
        st.image(details["image"],use_column_width=True)
        st.write(f"### 商品名稱：{product_name}")
        st.write(f"價格：{details["price"]}")
        st.write(f"庫存：{details["stock"]}")
        if st.button(f"購買{product_name}",key=product_name):
            if details["stock"] > 0:
                details["stock"] -= 1
                st.success("購買成功")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("庫存不足")
    i += 1

#新增商品庫存區塊
st.title("新增商品庫存")
product_name = list(st.session_state.products.keys())
#選擇要補貨的產品
cols = st.columns(2) #將對話框分成兩欄
with cols[0]:
    product_name = st.selectbox("請選擇要補貨的產品", product_name)
with cols[1]:
    stock = st.number_input("請輸入要補貨的庫存數量", min_value=1, step=1) 
if st.button("新增庫存",key=1): 
    st.session_state.products[product_name]["stock"] += stock #將庫存加到商品的庫存中
    st.success("補貨成功") #跳出補貨成功的訊息
    time.sleep(0.5)
    st.rerun()
for product_name,details in st.session_state.products.items(): 
    st.write(f"{product_name}: {details['stock']}")  # 印出商品名稱和庫存數量
