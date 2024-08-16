import streamlit as st
import openai  # pip install openai
from utils import load_openai_api

openai.api_key = load_openai_api()

prompt_text = st.text_area("Prompt", "A cute baby sea otter")  # 輸入提案文字
if st.button("開始生成圖片"):  # 按鈕
    generatedImage = openai.images.generate(  # 生成圖片
        model="dall-e-3",  # 選擇模型
        prompt=prompt_text,  # 輸入提案文字
        n=1,  # 設定生成圖片數量 目前最多只支援1張圖片
        size="1024x1024",  # 設定圖片大小
    )
    image_url = generatedImage.data[0].url  # 取得圖片網址
    st.image(image_url)
