### 函數與變數作用域的使用

1. **區域變數 (Local Variable)**:
   - 定義在函數內部的變數，只能在該函數內部使用，外部無法存取。例如：

     ```python
     def calculate_square_area():
         area = length**2  # area 是區域變數
         print("面積是：", area)
     ```

   - 如果函數內的變數名稱與全域變數相同，函數內部會優先使用區域變數。

2. **全域變數 (Global Variable)**:
   - 定義在函數外部的變數，可以在整個程式中使用。
   - 若要在函數內部修改全域變數，需使用 `global` 關鍵字。例如：

     ```python
     def calculate_square_area():
         global area  # 將 area 宣告為全域變數
         area = length**2  # 修改全域變數 area
     ```

3. **函數返回值 (Return Statement)**:
   - 使用 `return` 將區域變數的值返回，並可在外部接收。例如：

     ```python
     def calculate_square_area():
         area = length**2
         return area  # 返回區域變數
     ```

4. **函數參數**:
   - 傳入函數的參數視為區域變數，僅能在函數內部使用。例如：

     ```python
     def hello(name):
         print(f"hello {name}")
     ```

5. **函數說明文檔 (Docstring)**:
   - 使用 `""" """` 為函數撰寫說明文檔，描述函數功能、參數和返回值。例如：

     ```python
     def hello(name):
         """
         這是一個打招呼的函數
         參數:
         name: str - 名字
         返回值: None
         """
         print(f"hello {name}")
     ```

### Streamlit 的使用技巧

1. **Session State 管理**:
   - 使用 `st.session_state` 儲存和管理狀態資訊，能在多次互動中保留狀態。例如：

     ```python
     if "history" not in st.session_state:
         st.session_state.history = []  # 初始化對話紀錄
     ```

2. **UI 佈局**:
   - 使用 `st.columns` 分割頁面，將內容分佈在不同的列中。例如：

     ```python
     col1, col2, col3 = st.columns([4, 2, 1])
     ```

3. **互動與事件觸發**:
   - 使用按鈕來觸發事件，例如清空對話紀錄並重新整理頁面：

     ```python
     if st.button("清除對話紀錄"):
         st.session_state.history = []  # 清空對話紀錄
         st.rerun()  # 重新整理頁面
     ```

4. **檔案上傳與處理**:
   - 使用 `st.file_uploader` 來上傳圖片或文件，並進行處理。例如：

     ```python
     uploaded_file = st.file_uploader("上傳圖片", type=["png", "jpg", "jpeg"])
     if uploaded_file:
         st.image(uploaded_file, caption="圖片上傳成功", width=300)
     ```

### OpenAI API 使用技巧

1. **API 金鑰載入**:
   - 使用 `openai.api_key` 載入 API 金鑰，用於身份驗證和調用 API。例如：

     ```python
     openai.api_key = load_openai_api()
     ```

2. **文字生成**:
   - 利用 OpenAI API 生成文字回應，並可將用戶的輸入和系統訊息作為上下文提供。例如：

     ```python
     response = openai.chat.completions.create(
         model=st.session_state.model,
         temperature=0.1,
         messages=[{"role": "system", "content": st.session_state.system_message}]
         + st.session_state.history,
     )
     ```

3. **圖片生成與處理**:
   - 使用 DALL·E 生成圖片，設定圖片大小和輸出張數。例如：

     ```python
     generatedImage = openai.images.generate(
         model="dall-e-3",
         prompt=prompt_text,
         n=1,
         size="1024x1024",
     )
     image_url = generatedImage.data[0].url
     st.image(image_url)
     ```

4. **圖片分析與處理**:
   - 將上傳的圖片轉換為 base64 格式，並與提示詞一起發送給 OpenAI 進行分析。例如：

     ```python
     image_base64 = encode_image("temp_image.png")
     prompt = st.chat_input("輸入提示詞")
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
     ```
