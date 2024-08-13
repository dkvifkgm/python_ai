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
print(a, b)  # 複製a的值給b，所以a跟b指向不同的陣列，因此b的元素不會影響a

# append
L = [1, 2, 3]
L.append(4)  # 把4加到L的最後面
print(L)

# 陣列有兩種移除模式
# 1.remove  移除指定值
L = [1, 2, 3, 1]
L.remove(1)  # removec只會移除最前面的1

#
# pop 移除指定位置的元素，如果沒有指定就是刪除最後面的元素
L = [1, 2, 3]
print(L.pop(0))  # 刪除第一個元素
print(L.pop())  # 刪除最後一個元素

# extend
L = [1, 2, 3]
L.extend([4, 5, 6])
print(L)

# insert
L = [1, 2, 3]
L.insert(1, 4)
print(L)
