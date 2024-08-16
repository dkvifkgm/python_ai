import streamlit as st
import openai
from utils import load_openai_api, encode_image

openai.api_key = load_openai_api()

st.title("AT圖片分析")
# 上傳圖片
uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="圖片上傳成功", width=300)

    # 將上傳的文件轉換成臨時圖片
    with open("temp_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 將上傳的圖片轉換成base64
    image_base64 = encode_image("temp_image.png")

    prompt = st.chat_input("輸入提示詞")  # 顯示對話輸入框
    if prompt:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_base64}"
                            },
                        },
                    ],
                }
            ],
        )

        assistant_message = response.choices[0].message.content
        st.write(assistant_message)
