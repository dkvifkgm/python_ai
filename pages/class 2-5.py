# [] 陣列
print([])  # 空陣列
print([1, 2, 3])  # 陣列
print([1, 2, 3, "a", "b", "c", True, False])  # 陣列也可以有字串和布林值

# list 讀取陣列
L = [1, 2, 3, "a", "b", "c"]  # 宣告陣列
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # a

# len 陣列長度
L = [1, 2, 3, "a", "b", "c"]
print(len([1, 2, 3]))  # 6

# 走訪元素
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):
    print(L[i])  # 1, 2, 3, a, b, c
