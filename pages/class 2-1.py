# 比較運算值
print(1 == 1)  # 等於
print(1 != 1)  # 不等於
print(1 > 1)  # 大於
print(1 < 1)  # 小於
print(1 >= 1)  # 大於等於
print(1 <= 1)  # 小於等於

# 邏輯運算子
# and
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not
print(not True)  # False
print(not False)  # True

# 優先順序
# 1.() 括號
# 2.**次方
# 3.* / // 乘法 除法 取整除法
# 4.+ - 加法 減法
# 5. == != > < >= <= 判斷運算子
# 6. and or not 邏輯運算子
# 7. = += -= *= /= //= %= **= //= 算術指定運算子

# 密碼門
password = input("你是誰? ")  # 輸入密碼
if password == "你爹米奇":  # 如果
    print("爸爸!")  # 密碼正確
elif password == "兒子 快叫爸爸":  # elif=else if
    print("爸爸!")  # 密碼正確
else:  # 否則
    print("滾！")  # 密碼錯誤
# 連續使用if與使用elif的差別:
# 使用多個 if: 每個條件都會被獨立檢查，可能會導致多個條件都為真並執行對應的代碼。
# 使用 elif: 一旦有一個條件成立，後面的條件將不再檢查。
