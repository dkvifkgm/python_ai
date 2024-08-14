# 算術指定運算子
a = 1
a += 1  # a=a+1
print(a)  # 2
a -= 1  # a=a-1
print(a)  # 1
a *= 2  # a=a*2
print(a)  # 2
a /= 2  # a=a/2
print(a)  # 1
a //= 2  # a=a//2
print(a)  # 0
a %= 2  # a=a%2
print(a)  # 1
a **= 2  # a=a**2

# while 迴圈
# while 會搭配一個條件是來使用
# 條件式為 True 時才會執行
# 條件式為 False 會跳出迴圈
# 每次迴圈執行都會檢查條件有沒有變成 False
i = 0
while i < 5:  # 條件式為 i<5 時才會執行
    print(i)  # 印出i
    i += 1  # i=i+1

# break 強制跳出迴圈


while i < 5:  # 條件式為 i<5 時才會執行
    for j in range(5):  # 循環迴圈
        print(j)  # 印出j
        if j == 3:  # 如果j等於3就會跳出迴圈
            break  # 跳出迴圈
        i += 1

for i in range(5):  # 循環迴圈
    print(i)  # 印出i
    if i == 3:  # 如果i等於3就會跳出迴圈
        break  # 跳出迴圈
    i += 1

import random

# random.randrange()設定抽籤範圍的方式跟rage()相似
print(random.randrange(10))  # 隨機產生一個整數
print(random.randrange(1, 10))  # 設定隨機產生數字的種子
print(random.randrange(1, 10, 5))  # 設定隨機產生數字的種子

# randomint()需設定抽籤範圍
print(random.randint(1, 10))  # 1~6
