### Streamlit 基本使用技巧

#### 1. 標題與分隔線

```python
st.title("標題文字")
st.markdown("---")
```

- `st.title()` 用於顯示標題。
- `st.markdown("---")` 用於插入水平分隔線。

#### 2. 欄位佈局 (`columns`)

```python
col1, col2 = st.columns(2)
col1.button("按鈕1", key="1")
col2.button("按鈕2", key="2")
```

- `st.columns(2)` 將頁面分成兩欄。
- `col1.button()` 和 `col2.button()` 用於在不同欄位內顯示按鈕。

#### 3. 自定義欄位比例

```python
col1, col2 = st.columns([1, 2])
```

- 可以使用列表指定各欄位的比例，例如 `[1, 2]` 表示 `col2` 的寬度是 `col1` 的兩倍。

#### 4. `with` 語句

```python
with col1:
    st.button("按鈕1", key="8")
    st.button("按鈕2", key="9")
```

- `with` 語句內的所有元件都會被添加到 `col1` 中。

#### 5. 動態生成多個欄位

```python
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{1+1}", key=f"{i+10}")
```

- 使用 `st.columns(4)` 動態生成四個欄位，並在每個欄位中添加按鈕。

#### 6. 文字輸入框 (`text_input`)

```python
text = st.text_input("輸入文字", value="這是預設文字")
st.markdown(f"文字輸入的值為: {text}")
```

- `st.text_input()` 用於顯示文字輸入框，並可以設定預設值。
- `st.markdown()` 用於顯示輸入框中的內容。

### `session_state` 狀態管理

#### 7. 使用 `st.session_state` 儲存狀態

```python
if "ans" not in st.session_state:
    st.session_state.ans = 1
```

- 檢查 `st.session_state` 中是否存在變數，若不存在則進行初始化。

#### 8. 強制重新整理

```python
st.rerun()
```

- `st.rerun()` 用於重新執行程式。

### 迴圈結構

#### 9. `while` 迴圈

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

- `while` 迴圈會一直執行，直到條件為 `False`。

#### 10. `for` 迴圈

```python
for i in range(5):
    print(i)
```

- `for` 迴圈會依次執行每一個元素的操作。

#### 11. `break` 跳出迴圈

```python
if i == 3:
    break
```

- 當條件成立時，使用 `break` 跳出迴圈。

### 隨機數生成 (`random`)

#### 12. 生成隨機數

```python
import random

print(random.randint(1, 10))
```

- 使用 `random.randint(a, b)` 生成指定範圍 `[a, b]` 內的隨機整數。

### 異常處理 (`try-except`)

#### 13. 捕捉異常

```python
try:
    number = int(input("請輸入一個數字"))
except:
    print("不要亂輸入啊！")
```

- `try-except` 結構用於捕捉並處理程式中可能出現的錯誤。
