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
# 可透過取得index的方式找到list中的資料
# 也可以把list當作一個範圍來取得資料
# 視情況決定有使用哪種方式
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])  # 1, 3, a

print(L[::2])  # 1, 3, a
print(L[1:3])  # 2, 3
print(L[1:3:2])  # 2

for i in L:
    print(i)

#:: = range

# 改變陣列元素的資料

# call by value
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # 2, 2, 3 因為a跟b指向同一個陣列，所以改變b的元素會影響a

# call by reference
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # 1, 2, 3 因為a跟b指向不同的陣列，所以改變b的元素會不會影響a
