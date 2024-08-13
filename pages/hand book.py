import streamlit as st

with st.expander("class 1課程筆記"):
    st.markdown(
        """ 
### 單行註解

```python
# 單行註解
```

- 使用 `#` 開頭來添加單行註解，通常用來對代碼進行簡單的說明。

### 多行註解

```python
'''
多行註解
'''
```

- 使用三個雙引號 `'''` 來添加多行註解。適用於對較大段代碼進行詳細說明。

### 基本型態

```python
print(1)  # 整數
print(1.0)  # 小數點
print("hello")  # 字串
print(True)  # 布林值
print(None)  # 空值
```

- `int`: 整數型態。
- `float`: 小數型態。
- `str`: 字串型態。
- `bool`: 布林值型態 (`True` 或 `False`)。
- `None`: 空值，用來表示不存在的值。

### 變數

```python
a = 1  # 宣告變數 將1存入變數a
print(a)  # 顯示變數a
a = a + 1  # 將a的值加1
print(a)  # 顯示變數a
```

- 變數的宣告與賦值使用等號 `=` 進行。
- 變數可以重新賦值。

### 運算子

```python
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取整除法
print(1 % 1)  # 取餘數
```

- `+`: 加法運算。
- `-`: 減法運算。
- `*`: 乘法運算。
- `/`: 除法運算，結果為浮點數。
- `//`: 整除運算，結果為整數。
- `%`: 取餘數。

### 運算子優先順序

```python
# 1. () 括號
# 2. ** 次方
# 3. * / // 乘法、除法、取整除法
# 4. + - 加法、減法
```

- 括號優先計算，其次是次方運算，再來是乘法、除法和取整除法，最後是加法和減法。

### 字串運算

```python
print("hello " + "world!")  # 字串加字串
print("hello!" * 3)  # 字串重複3次
```

- `+`: 用於字串連接。
- `*`: 用於重複字串。

### 字串格式化

```python
name = "john"
age = 20
print(f"hello my name is {name} and i am {age} years old")  # 字串格式化
```

- 使用 `f-string` 進行字串格式化，變數或表達式可以直接放入 `{}` 中。

### 內建函數 `len` 與 `type`

```python
print(len("hello"))  # 字串長度
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("hello"))  # <class 'str'>
```

- `len()`: 回傳字串的長度。
- `type()`: 回傳資料物件的類型。

### 型態轉換

```python
print(int("123"))  # 轉為int
print(float("123.456"))  # 轉為float
print(bool("1"))  # 轉為bool
print(str(123))  # 轉為str
```

- `int()`: 將字串或浮點數轉換為整數。
- `float()`: 將字串或整數轉換為浮點數。
- `bool()`: 將其他型態轉換為布林值。
- `str()`: 將其他型態轉換為字串。

### 使用 `input()` 取得使用者輸入

```python
a = int(input("請輸入園的半徑: "))  # 輸入整數
a = a**2  # 計算平方
print(a)  # 輸出結果
```

- `input()`: 從終端機取得使用者輸入。返回的值通常是字串，需要轉換為適當的型態。

### 使用 `Streamlit` 製作簡單的網頁介面

```python
import streamlit as st

st.markdown(
    '''
# 這是最大標題

- 項目一:
- 項目二:
- 項目三:

## 這是第二大標題

~~~python

# 程式碼區塊

~~~
'''
)
```

- `Streamlit`: 一個用於建立資料應用的 Python 庫。
- `st.markdown()`: 使用 Markdown 語法來顯示格式化文本。
"""
    )
