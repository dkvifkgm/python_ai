# dict是一個字典，可以儲存不同的鍵值對
# dict是透過key value的方式來存資料，key是唯一的，value可以重複
# dict是無序的，所以無法透過index來存取
# dict的key必須是不可變得資料型態
# dict的value可以是任意的資料型態
# dict的key_value是透過冒號來連接,key:value
# dict的key_value是透過逗號來分隔

d = {"a": 1, "b": 2, "c": 3}

# 取得dict的key
print(d.values())  # dict_{"a", "b", "c"}
for key in d.keys():
    print(key)

# 取得dict的value
for value in d.values():
    print(value)

# 取得dict的key_value
print(d.items())  # dict_{("a", 1), ("b", 2), ("c", 3)}
for key, value in d.items():
    print(key, value)

# 新增key_value
d["d"] = 4  # 新增
print(d)  # dict_{"a": 1, "b": 2, "c": 3, "d": 4}

# 修改key_value
d["c"] = 5
print(d)  # dict_{"a": 5, "b": 2 , "c": 5, "d": 4}

# 檢查dict是否存在某個key
# in無法檢查value
# 跟list比較，in檢查的是list的元素跟dict的key

# 刪除key_value 使用pop()
# 如果資料存在 則刪除並回傳value
print(d.pop("a"))  # 5
# 如果資料不存在 則回傳預設值
print(d.pop("e", "Not found"))  # Not found
# 如果資料不存在也沒有預設值 就會報錯

# 比較複雜的dict
d = {
    "a": {
        1,
        2,
        3,
    },
    "b": {"c": 4, "d": 5},
}
print(d["a"])  # {1, 2, 3}
print(d["b"][0])  # 1
print(d["b"])  # {"c": 4, "d": 5}
print(d["b"]["c"])  # 4

# 例:成績登記系統 key:為學生姓名 value:為學生成績 每個科目有三個成績
grade = {
    "張三": {"國文": [90, 80, 100], "英語": [80, 70, 90], "數學": [70, 60, 80]},
    "小美": {"國文": [80, 70, 90], "英語": [70, 60, 80], "數學": [60, 50, 70]},
    "李四": {"國文": [70, 60, 80], "英語": [60, 50, 70], "數學": [50, 40, 60]},
}

# 取得學生成績
print(grade["張三"]["英語"])  # 80,70,90
# 取得小美第一個國文成績
print(grade["小美"]["國文"][0])  # 80
# 取得小美第三個英語成績
print(grade["小美"]["英語"][2])  # 70

# 計算平均成績
for name, subjects in grade.items():
    total = 0  # 將total這個變數設為0
    for scores in subjects.values():
        total += sum(scores)
    avg = total / len(subjects) * 3
    print(f"{name} 的平均成績為 {avg}")

# 整理全校各科平均成績
# 建立一個dict用來存放各科目成績
avg_grade = {"國文": [], "英語": [], "數學": []}
# 逐一取得每為同學各科的成績
for subject in grade.items():
    # 逐一取得每個科目的成績
    for scores in subject.values():
        # 將新成績加入avg_grade
        avg_grade[subject] += sum(scores)
print(avg_grade)
