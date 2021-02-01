# 印出當月份日期及星期
# 範例：2020/11/17 (二)：

## 導入 datatime 模組 (為了獲取系統時間)
import datetime
# 讀取系統時間中的西元年份 (用於日期的印出)
year = datetime.date.today().year

### function "print_date"
## 參數說明
# month：月份 (1~12)
# week_number：當月一號從星期幾開始 (用數字 1~7 代替中文字)
# Feb_leap_or_not：二月是否遇到閏年 (預設 = 28 天，非閏年。閏年需設定為 29)
def print_date(month, week_number):
    # 生成一個數字 1~12 的 tuple (if 條件檢查用)
    month_tuple = tuple(i for i in range(1, 13))
    # 生成一個數字 1~7 的 tuple (if 條件檢查用)
    week_number_tuple = tuple(i for i in range(1, 8))

    # 如果 month & week_number 的引數都有在 tuple 裡 (月份符合 1~12，星期符合 1~7)，則執行印出程式
    if (week_number in week_number_tuple) and (month in month_tuple):
        # 先形成一個中文字一到日、重複 7 次的 tuple，用於印出中文的星期
        week = ("一", "二", "三", "四", "五", "六", "日")*7

        # 如 month == 1, 3, 5, 7, 8 月，印出時月份前加 0，共要印出 31 天份的日期
        if month in (1, 3, 5, 7, 8):
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/0{}/0{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 31):
                print("{}/0{}/{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()

        # 如 month == 10, 12 月，印出時月份前不加 0，共要印出 31 天份的日期
        elif month in (10, 12):
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/{}/0{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 31):
                print("{}/{}/{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()

        # 如 month == 4, 6, 9 月，印出時月份前加 0，共要印出 30 天份的日期
        elif month in (4, 6, 9):
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/0{}/0{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 30):
                print("{}/0{}/{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()

        # 如 month == 11 月，印出時月份前不加 0，共要印出 30 天份的日期
        elif month == 11:
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/{}/0{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 30):
                print("{}/{}/{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                print()

        # 如 month == 2 月，則先判斷年份為閏年 or 平年，再印出相應的日期數 (閏年 29 天、平年 28 天)
        if month == 2:
            # 閏年判斷式 (如結果為 True，則 year 為閏年)，通過則印出 29 天
            if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)):
                for i in range(9):
                    print("{}/0{}/0{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                    print()
                for i in range(9, 29):
                    print("{}/0{}/{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                    print()
            # 閏年判斷式回傳 False (year 為平年)，則印出 28 天
            else:
                for i in range(9):
                    print("{}/0{}/0{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                    print()
                for i in range(9, 28):
                    print("{}/0{}/{} ({})：".format(year, month, i + 1, week[i + (week_number - 1)]))
                    print()

    # 如只有 week_number 引數在 week_number_tuple 裡，則印出 "月份輸入超出範圍" 訊息
    elif week_number in week_number_tuple:
        print("錯誤！月份範圍限於 1~12")
    # 如只有 month 引數在 month_tuple 裡，則印出 "星期數字輸入超出範圍" 訊息
    elif month in month_tuple:
        print("錯誤！星期數字範圍限於 1~7")
    # 如 month & week_number 引數都不在各自 tuple 範圍，則印出 "月份及星期數字皆超出範圍" 訊息
    else:
        print("錯誤！月份及星期數字皆超出範圍")


# Date_function.py 測試程式
if __name__ == "__main__":
    # 測試預設情況
    print_date(6, 2)
    # 分隔線
    print("---------------------")
    # 測試 2 月自動判斷閏年印出情況
    print_date(2, 2)
    # 分隔線
    print("---------------------")
    # 測試輸入月份超出範圍情況
    print_date(13, 1)
    # 測試輸入星期超出範圍情況
    print_date(3, 8)
    # 測試月份及星期皆超出範圍的情況
    print_date(13, 9)
