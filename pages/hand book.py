import streamlit as st
import os

folderPath = "markdown"
files = os.listdir(folderPath)
# 篩選要的檔案
files_name = []  # 新增資料夾用來存放md檔
for f in files:  # 逐一檢查每個檔案
    if f.endswith(".md"):  # 如果檔案名稱的結尾是.md
        files_name.append(f)  # 將檔案名稱加入到files_name列表中
print(files_name)

for f in files_name:  # 逐一讀取所有.md檔
    with open(folderPath + "/" + f, "r", encoding="utf-8") as files:  # 讀取檔案
        content = files.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 使用expander，標題為檔案名稱去掉.md
        st.markdown(content)  # 將檔案內容加入到expander中
