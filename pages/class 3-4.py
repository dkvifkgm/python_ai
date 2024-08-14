import random

print("猜數字遊戲")
smail = 1
big = 100
guest = random.randint(1, 100)
number = 0

while number < guest or number > guest:
    # try跟except是一對的 可以讓程式在有錯誤時停止運行
    try:
        number = int(input("請輸入一個" + str(smail) + "~" + str(big) + "的數字 "))
    except:
        print("不要亂輸入啊！")
        continue
    if number > guest:
        print("你猜得太大了")
        if number < big:
            big = number
        else:
            big = big
    else:
        print("你猜得太小了")
        if number > smail:
            smail = number
        else:
            smail = smail
print("恭喜你，正確！")
