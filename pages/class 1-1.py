# 單行註解

"""
多行註解
"""

# 基本型態
print(1)  # 整數
print(1.0)  # 小數點
print("hello")  # 字串
print(True)  # 布林值
print(None)  # 空值

# 變數
# print(max(1, 2, 3))  # 最大值
# print(min(1, 2, 3))  # 最小值
# print(sum(1, 2, 3))  # 總和
# print(len(1, 2, 3))  # 長度

# 變數
a = 1  # 宣告變數 將1存入變數a
print(a)  # 顯示變數a
a = a + 1  # 將a的值加1
print(a)  # 顯示變數a

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取整除法
print(1 % 1)  # 取餘數

# 優先順序
# 1.() 括號
# 2.**次方
# 3.* / // 乘法 除法 取整除法
# 4.+ - 加法 減法

# 字串運算 +跟*
print("hello " + "world!")  # 字串加字串
print("hello!" * 3)  # 字串重複3次

# 字串格式化
name = "john"  # 宣告字串
age = 20  # 宣告整數
print(f"hello my name is {name} and i am {age} years old")  # 字串格式化
# 可以將變數或其他型態的資料放到f字串的{}中

# len 字串長度
print(len("hello"))

# type 資料物件類型
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("hello"))  # <class 'str'>

# 轉換型態
print(int("123"))  # float轉int
print(float("123.456"))  # int轉float
print(bool("1"))  # int轉bool
print(bool("0"))  # int轉bool
print(str(123))  # int轉str
print(str(123.456))  # float轉str
