### Python 字典 (dict) 筆記

#### 1. 字典的基本概念

- **字典 (dict)** 是一種資料結構，用於儲存**鍵值對 (key-value pairs)**。
- **Key (鍵)** 是唯一的，用來標識每個值 (value)，而值可以是任何資料型態且可以重複。
- 字典是**無序的**，因此不能像列表一樣透過索引來存取元素。
- 字典的鍵必須是**不可變的資料型態**，例如字串、數字或元組。

#### 2. 字典的語法

- 字典的鍵值對透過**冒號 `:`** 來連接，例如：`key: value`。
- 多個鍵值對之間使用**逗號 `,`** 來分隔。

```python
# 定義一個字典
d = {"a": 1, "b": 2, "c": 3}
```

#### 3. 取得字典的鍵和值

- 使用 `d.keys()` 可以取得字典的所有鍵。
- 使用 `d.values()` 可以取得字典的所有值。
- 使用 `d.items()` 可以取得字典的所有鍵值對。

```python
# 取得鍵
print(d.keys())  # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)

# 取得值
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)

# 取得鍵值對
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)
```

#### 4. 新增和修改字典的鍵值對

- 使用 `d["key"] = value` 新增或修改字典中的鍵值對。

```python
# 新增鍵值對
d["d"] = 4
print(d)  # {"a": 1, "b": 2, "c": 3, "d": 4}

# 修改鍵值對
d["c"] = 5
print(d)  # {"a": 1, "b": 2, "c": 5, "d": 4}
```

#### 5. 檢查字典中是否存在某個鍵

- 使用 `in` 檢查字典中是否存在某個鍵。

```python
if "a" in d:
    print("Key 'a' is in the dictionary.")
```

#### 6. 刪除字典中的鍵值對

- 使用 `d.pop(key)` 刪除字典中的鍵值對，如果鍵存在，返回其對應的值；如果鍵不存在，可以設定預設返回值。

```python
# 刪除並返回鍵的值
print(d.pop("a"))  # 1
# 如果鍵不存在，返回預設值
print(d.pop("e", "Not found"))  # "Not found"
```

#### 7. 複雜的字典結構

- 字典中的值可以是另一個字典或集合等複雜資料結構。

```python
d = {
    "a": {1, 2, 3},
    "b": {"c": 4, "d": 5},
}

print(d["a"])  # {1, 2, 3}
print(d["b"]["c"])  # 4
```

#### 8. 例子：成績登記系統

- 這是一個使用字典儲存學生成績的例子，每個學生的成績由多個科目組成，每個科目有多個分數。

```python
grade = {
    "張三": {"國文": [90, 80, 100], "英語": [80, 70, 90], "數學": [70, 60, 80]},
    "小美": {"國文": [80, 70, 90], "英語": [70, 60, 80], "數學": [60, 50, 70]},
    "李四": {"國文": [70, 60, 80], "英語": [60, 50, 70], "數學": [50, 40, 60]},
}

# 取得學生成績
print(grade["張三"]["英語"])  # [80, 70, 90]
print(grade["小美"]["國文"][0])  # 80

# 計算每位學生的平均成績
for name, subjects in grade.items():
    total = sum(sum(scores) for scores in subjects.values())
    avg = total / (len(subjects) * 3)
    print(f"{name} 的平均成績為 {avg}")

# 計算全校各科平均成績
avg_grade = {"國文": 0, "英語": 0, "數學": 0}
for subjects in grade.values():
    for subject, scores in subjects.items():
        avg_grade[subject] += sum(scores)

print(avg_grade)
```

---

### Streamlit 筆記

#### 1. 基本元件使用

- **st.title("標題")**：設定頁面的標題。
- **st.image(圖片路徑, 寬度)**：顯示圖片，可設定圖片寬度。
- **st.number_input("標題", min_value, max_value, step, value)**：數字輸入框，設置輸入值範圍與步進值。

```python
import streamlit as st

st.title("圖片元件")
st.image("image/apple.png", width=100)
image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)
```

#### 2. 顯示多張圖片

- 使用 **os.listdir()** 獲取資料夾中的所有檔案名稱，並逐一顯示。

```python
import os
image_folder = "image"
image_files = os.listdir(image_folder)

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
```

#### 3. 使用 Streamlit session state

- 使用 **st.session_state** 來儲存跨回合的資料，例如商品庫存。

```python
if "products" not in st.session_state:
    st.session_state.products = {}

for image_file in image_files:
    product_name = image_file[:-4]
    if product_name not in st.session_state.products:
        st.session_state.products[product_name] = {"price": 10, "stock": 10, "image": f"{image_folder}/{image_file}"}
```

#### 4. 顯示商品並實現購物功能

- 使用 **st.columns()** 將頁面分割成多欄來顯示商品。

```python
col_number = st.number_input("請輸入商品欄數", min_value=1, max_value=10, step=1)
cols = st.columns(col_number)

for i, (product_name, details) in enumerate(st.session_state.products.items()):
    with cols[i % col_number]:
        st.image(details["image"], use_column_width=True)
        st.write(f"### 商品名稱：{product_name}")
        st.write(f"價格：{details['price']}")
        st.write(f"庫存：{details['stock']}")
        if st.button(f"購買{product_name}", key=product_name):
            if details["stock"] > 0:
                details["stock"] -= 1
                st.success("購買成功")
                st.rerun()
            else:
                st.error("庫存不足")
```

#### 5. 新增商品庫存

- 使用者可以透過介面補貨，並立即更新顯示。

```python
product_name = list(st.session_state.products.keys())
cols = st.columns(2)
with cols[0]:
    selected_product = st.selectbox("請選擇要補貨的產品", product_name)
with cols[1]:
    stock = st.number_input("請輸入要補貨的庫存數量", min_value=1, step=1)
if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += stock
    st.success("補貨成功")
    st.rerun()
```

---

### 函數 (Function) 筆記

#### 1. 基本函數定義

- 使用 **def 函數名稱(參數):** 來定義一個函數。
- 函數內可以使用 `return` 回傳值。

```python
def hello():
    print("hello")

for i in range(10):
    hello()
```

#### 2. 帶參數的函數

- 可以在定義函數時加入參數，呼叫函數時傳入具體值。

```python
def hello(name):
    print(f"hello {name}")

hello("John")
```

#### 3. 帶回傳值的函數

- 使用 `return` 將結果回傳給呼叫者。

```python
def add

(a, b):
    return a + b

sum = add(3, 4)
print(sum)  # 7
```

#### 4. 多個回傳值的函數

- 函數可以回傳多個值，使用逗號分隔。

```python
def add_sub(a, b):
    return a + b, a - b

sum, sub = add_sub(5, 3)
print(sum, sub)  # 8 2
```

#### 5. 預設參數值

- 可以在定義函數時為參數設置預設值，未傳入值時會使用預設值。

```python
def hello(name, message="hello"):
    print(f"{message} {name}")

hello("John")  # hello John
hello("Tom", "good morning")  # good morning Tom
```

#### 6. 限制參數型態

- 可以在參數宣告時限制其型態。

```python
def add(a: int, b: int = 0):
    return a + b

print(add(1, 2))  # 3
```
