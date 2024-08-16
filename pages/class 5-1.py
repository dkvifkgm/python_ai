# def 區域變數
length = 10


def calculate_square_area():
    area = length**2
    # lenght事權域變數 因為並沒有設定初始值，所以會優先去行程式望尋找想同名稱的變數
    # length = length + 1 會出錯
    # 因為在函數內部，length是區域變數，因此不能直接修改全域變數
    # area不能在外面使用，因為這個函數是區域變數
    print("面積是：", area)


calculate_square_area()

length = 5


def calculate_square_area():
    area = length**2
    print("面積是：", area)


length = 10
calculate_square_area()
# 因為這邊才召喚了def calculate_square_area()，而在這行程式前，最終liength=10，所以最終執行結果會是100

length = 5  # 全域變數
area = 3.14 * 10**2  # 全域變數


def calculate_square_area():
    area = length**2  # area是區域變數 length是全域變數


calculate_square_area()
print("面積是：", area)  # 區域變數不能在外面使用，所以這個area是外面的area
# 執行結果會是100

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # area是區域變數 length是全域變數
    return area  # 把區域變數丟出去


area = calculate_square_area()  # 將
print("面積是：", area)  # 面積是25

length = 5
area = 3.14 * 10**2


def calculate_square_area():
    global area  # 使用global，將area變成全域變數
    area = length**2


calculate_square_area()
print("面積是：", area)  # 面積是25


def hello(name):  # 函數傳入的參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數\n
    name: str-名字\n
    回傳 none\n
    範例\n
    """
    print(f"hello {name}")
