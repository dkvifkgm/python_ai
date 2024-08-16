### 函數與區域變數的使用

1. **區域變數 (Local Variable)**:
   - 函數內部定義的變數是區域變數，僅能在該函數內部使用，外部無法存取。例如：

     ```python
     def calculate_square_area():
         area = length**2  # 這裡的 area 是區域變數
         print("面積是：", area)
     ```

   - 當區域變數名稱與全域變數名稱相同時，函數內會優先使用區域變數。

2. **全域變數 (Global Variable)**:
   - 在函數外部定義的變數是全域變數，可以在整個程式中使用。
   - 若要在函數內部修改全域變數，需使用 `global` 關鍵字。例如：

     ```python
     length = 5  # 全域變數
     area = 100  # 全域變數

     def calculate_square_area():
         global area  # 使用 global 關鍵字將 area 變成全域變數
         area = length**2  # 修改全域變數 area
     ```

3. **函數參數**:
   - 函數的參數也視為區域變數。例如：

     ```python
     def hello(name):
         print(f"hello {name}")
     ```

### Streamlit 常用技巧

1. **Session State**:
   - Streamlit 中使用 `st.session_state` 儲存及管理狀態資訊。例如：

     ```python
     if "history" not in st.session_state:
         st.session_state.history = []  # 初始化對話紀錄
     ```

2. **UI 元素與佈局**:
   - 利用 `st.columns` 分割頁面。例如：

     ```python
     col1, col2, col3 = st.columns([4, 2, 1])
     ```

   - 利用 `st.text_input` 接收文字輸入：

     ```python
     st.session_state.system_message = st.text_input("系統訊息", st.session_state.system_message)
     ```

3. **互動與事件觸發**:
   - 使用按鈕觸發事件：

     ```python
     if st.button("清除對話紀錄"):
         st.session_state.history = []  # 清空對話紀錄
         st.rerun()  # 重新整理頁面
     ```

   - 使用 `st.chat_input` 接收用戶輸入：

     ```python
     prompt = st.chat_input("請輸入想要對話的訊息")
     ```

### OpenAI API 使用

1. **API 金鑰載入**:
   - 使用 `openai.api_key` 載入 API 金鑰：

     ```python
     openai.api_key = load_openai_api()
     ```

2. **文字生成**:
   - 利用 OpenAI API 生成回應訊息：

     ```python
     responce = openai.chat.completions.create(
         model=st.session_state.model,
         temperature=0.1,
         messages=[{"role": "system", "content": st.session_state.system_message}]
         + st.session_state.history,
     )
     ```

3. **圖片生成**:
   - 使用 DALL·E 生成圖片：

     ```python
     generatedImage = openai.images.generate(
         model="dall-e-3",
         prompt=prompt_text,
         n=1,
         size="1024x1024",
     )
     ```

### 指令說明區

- 在函數前使用 `""" """` 來撰寫函數的說明文檔。例如：

  ```python
  def hello(name):
      """
      指令說明區
      這是一個打招呼的函數
      參數
      name: str - 名字
      回傳 none
      範例
      """
      print(f"hello {name}")
  ```
