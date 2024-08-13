## 1. 比較運算子

- `==` : 判斷兩個值是否相等。

    ```python
    print(1 == 1)  # True
    ```

- `!=` : 判斷兩個值是否不相等。

    ```python
    print(1 != 1)  # False
    ```

- `>` : 判斷左邊的值是否大於右邊的值。

    ```python
    print(1 > 1)  # False
    ```

- `<` : 判斷左邊的值是否小於右邊的值。

    ```python
    print(1 < 1)  # False
    ```

- `>=` : 判斷左邊的值是否大於或等於右邊的值。

    ```python
    print(1 >= 1)  # True
    ```

- `<=` : 判斷左邊的值是否小於或等於右邊的值。

    ```python
    print(1 <= 1)  # True
    ```

## 2. 邏輯運算子

- `and` : 兩個條件都為真時，結果才為真。

    ```python
    print(True and True)  # True
    print(True and False)  # False
    ```

- `or` : 只要有一個條件為真，結果就為真。

    ```python
    print(True or True)  # True
    print(True or False)  # True
    ```

- `not` : 反轉布林值。

    ```python
    print(not True)  # False
    ```

## 3. 優先順序

運算子的優先順序如下：

1. `()` : 括號
2. `**` : 次方
3. `* / //` : 乘法、除法、取整除法
4. `+ -` : 加法、減法
5. `== != > < >= <=` : 比較運算子
6. `and or not` : 邏輯運算子

## 4. 條件判斷 (if, elif, else)

- `if` : 用來判斷條件是否成立，若成立則執行對應的程式碼。
- `elif` : 當前面的`if`條件不成立時，才會檢查`elif`條件。
- `else` : 當前面的所有條件都不成立時，執行`else`裡的程式碼。

    ```python
    password = input("你是誰? ")
    if password == "你爹米奇":
        print("爸爸!")
    elif password == "兒子 快叫爸爸":
        print("爸爸!")
    else:
        print("滾！")
    ```

## 5. Streamlit

- `st.number_input()` : 用於在Streamlit應用程式中生成數字輸入框。

    ```python
    number = st.number_input("請輸入一個數字", min_value=0, max_value=100)
    ```

- `st.markdown()` : 用於在Streamlit中渲染Markdown格式的文本。

    ```python
    st.markdown(f"你輸入的數字是 {number}")
    ```

- `st.title()` : 用於在Streamlit中顯示標題。

    ```python
    st.title("練習")
    ```

## 6. 迴圈 (for)

- `for` 迴圈用於重複執行程式碼，通常與`in`和`range()`搭配使用。
- `range()` : 用於生成一個數字範圍，`range(start, stop, step)` 可以指定起始值、結束值和間隔值。

    ```python
    for i in range(10):  # 0到9
        print(i)
    ```

- `for` 迴圈也可以遍歷陣列中的每個元素。

    ```python
    for i in L:
        print(i)
    ```

## 7. 陣列 (List)

- 空陣列：`[]`。

    ```python
    print([])  # []
    ```

- 陣列可以包含不同類型的元素。

    ```python
    print([1, 2, 3, "a", "b", "c", True, False])  # [1, 2, 3, 'a', 'b', 'c', True, False]
    ```

- 透過`[]`來存取陣列中的元素。

    ```python
    L = [1, 2, 3, "a", "b", "c"]
    print(L[0])  # 1
    ```

## 8. 陣列操作

- `len()` : 返回陣列的長度。

    ```python
    L = [1, 2, 3, "a", "b", "c"]
    print(len(L))  # 6
    ```

- 使用`range()`與索引來遍歷部分元素。

    ```python
    for i in range(0, len(L), 2):
        print(L[i])  # 1, 3, a
    ```

- `list slicing` : 切片操作可以用來獲取陣列的一部分。

    ```python
    print(L[::2])  # [1, 3, 'a']
    print(L[1:3])  # [2, 3]
    print(L[1:3:2])  # [2]
    ```

- `call by value` : 在複製陣列時，修改複製的陣列不會影響原始陣列。

    ```python
    a = [1, 2, 3]
    b = a.copy()
    b[0] = 2
    print(a, b)  # [1, 2, 3] [2, 2, 3]
    ```

- `append()` : 將新元素添加到陣列的末尾。

    ```python
    L = [1, 2, 3]
    L.append(4)
    print(L)  # [1, 2, 3, 4]
    ```

- `remove()` : 移除陣列中第一個匹配的元素。

    ```python
    L = [1, 2, 3, 1]
    L.remove(1)  # 只會移除第一個1
    print(L)  # [2, 3, 1]
    ```

- `pop()` : 根據索引位置移除元素，若無參數則移除最後一個元素。

    ```python
    L = [1, 2, 3]
    print(L.pop(0))  # 1
    print(L.pop())  # 3
    print(L)  # [2]
    ```

- `extend()` : 將另一個陣列的元素添加到當前陣列的末尾。

    ```python
    L = [1, 2, 3]
    L.extend([4, 5, 6])
    print(L)  # [1, 2, 3, 4, 5, 6]
    ```

- `insert()` : 在指定索引位置插入新元素。

    ```python
    L = [1, 2, 3]
    L.insert(1, 4)
    print(L)  # [1, 4, 2, 3]
    ```
