import streamlit as st
import os

st.title("圖片元件")
# st.image指令 ，參數(圖片檔案路徑，寬度)
st.image("image/apple.png", width=100)

image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾內所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input(
    "圖片大小", min_value=50, max_value=500, step=50, value=100
)  # 取得圖片大小
# 使用者輸入圖片大小,最小50,最大500,每次取值50,初始值100

# image_file 會依次取出 image_files 裡面的一個項目（比如檔案名或檔案物件）
for image_file in image_files:
    # 顯示圖片 並依照使用者輸入大小調整寬度
    st.image(f"{image_folder}/{image_file}", width=image_size)

# image_file 會依次取出 image_files 裡面的一個項目（比如檔案名或檔案物件）
for image_file in image_files:
    # 除了with,還有use_columns,_width可以使用 會將圖片寬度設為欄寬度
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片 使用欄寬度
