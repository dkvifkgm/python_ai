# def
# 新增一個函數要用def開頭，後面接著函數名稱 在接上小括弧 最後接上冒號
# 小括弧裡面可以放傳入的參數也可以不放
def hello():
    print("hello")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數有一個參數 name 當呼叫這個函數 可以傳入一筆資料進去
def hello(name):
    print(f"hello {name}")


hello("john")
hello("mary")
hello("tom")
for i in range(10):
    hello(i)  # 這裡的i會被當作name的值


# 有回傳值的函數
# 這個函數會回傳一個值，當呼叫這個函數時，可以把這個值存到一個變數中
# 在指令當中只要執行return，就會回傳一個值，並結束函數
def add(a, b):
    return a + b


print(add(1, 2))
print(add("Hello", "World!"))
sum = add(3, 4)  # 可以將回傳值存到一個變數中
print(sum)


# 有多個回傳值的函數
# 這個函數會回兩個值，當呼叫這個函數時，可以把這個值存起來
def add(a, b):
    return a + b, a - b


sum, sub = add(3, 4)  # 可以將回傳值存到一個變數中
print(sum)
print(sub)


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數定義中加入預設參數，當呼叫函數時，如果沒有指定參數，就會使用預設值
# 多個參數時，
# 多個參數時 有預設值的參數要放在最後
def hello(name, massage="hello"):
    print(f"{massage} {name}")


hello("john")
hello("tom", "good morning")


# 限制傳入的參數型態
# 可以在函數的參數中設定型態，當呼叫函數時，可提示使用者要輸入的參數型態
def add(a: int, b: int = 0):
    return a + b


print(add(1, 2))
print(add("Hello", "World!"))
