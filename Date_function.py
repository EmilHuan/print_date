# 印出當月份日期及星期
# 範例：2020/11/17 (二)：

## 導入 datatime 模組 (為了獲取系統時間)
import datetime
# 讀取系統時間中的西元年份 (用於日期的印出)
year = datetime.date.today().year


### 印出空格 function (可自訂要空幾格)
def blank_rows(number):
    number += 1
    for i in range(1, number):
        i += 1
        print("")


### function "print_date"
## 參數說明
# month：月份 (1~12)
# week_number：當月一號從星期幾開始 (用數字 1~7 代替中文字)
# Feb_leap_or_not：二月是否遇到閏年 (預設 = 28 天，非閏年。閏年需設定為 29)
# blank_number：作為 blank_rows() 的引數，自訂空格數用
def print_date(month, blank_number = 1):
    # 生成一個數字 1~12 的 tuple (if 條件檢查用)
    month_tuple = tuple(i for i in range(1, 13))

    # 如果 month 的引數有在 month_tuple 裡 (月份符合 1~12)，則執行印出程式
    if month in month_tuple:
        # 先形成一個中文字一到日、重複 7 次的 tuple，用於印出中文的星期
        week_ch = ("一", "二", "三", "四", "五", "六", "日") * 7

        ## 用 datetime 模組回傳使用者輸入月份 (month) 的 1 號是星期幾
        # 將系統年份、使用者輸入月份 (month) 的 1 號設為變數 day (e.g 2021-07-01 00:00:00)
        day = datetime.datetime(year, month, 1)
        # 回傳 day 這天是出星期幾 (數字) 給變數 week_number
        week_number = day.isoweekday()

        # 如 month == 1, 3, 5, 7, 8 月，印出時月份前加 0，共要印出 31 天份的日期
        if month in (1, 3, 5, 7, 8):
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/0{}/0{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                # 使用 blank_rows 函數設定每個印出的日期要空幾格
                blank_rows(blank_number)
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 31):
                print("{}/0{}/{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)

        # 如 month == 10, 12 月，印出時月份前不加 0，共要印出 31 天份的日期
        elif month in (10, 12):
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/{}/0{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 31):
                print("{}/{}/{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)

        # 如 month == 4, 6, 9 月，印出時月份前加 0，共要印出 30 天份的日期
        elif month in (4, 6, 9):
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/0{}/0{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 30):
                print("{}/0{}/{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)

        # 如 month == 11 月，印出時月份前不加 0，共要印出 30 天份的日期
        elif month == 11:
            # 1~ 9 號印出時，日期前面加 0
            for i in range(9):
                print("{}/{}/0{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)
            # 9~31 號印出時，日期前面不加 0
            for i in range(9, 30):
                print("{}/{}/{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                blank_rows(blank_number)

        # 如 month == 2 月，則先判斷年份為閏年 or 平年，再印出相應的日期數 (閏年 29 天、平年 28 天)
        if month == 2:
            # 閏年判斷式 (如結果為 True，則 year 為閏年)，通過則印出 29 天
            if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
                for i in range(9):
                    print("{}/0{}/0{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                    blank_rows(blank_number)
                for i in range(9, 29):
                    print("{}/0{}/{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                    blank_rows(blank_number)
            # 閏年判斷式回傳 False (year 為平年)，則印出 28 天
            else:
                for i in range(9):
                    print("{}/0{}/0{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                    blank_rows(blank_number)
                for i in range(9, 28):
                    print("{}/0{}/{} ({})：".format(year, month, i + 1, week_ch[i + (week_number - 1)]))
                    blank_rows(blank_number)

    # 如 month 引數不在 month_tuple 範圍 (輸入月份超出 1~12)，則印出 "月份輸入超出範圍" 訊息
    else:
        print("錯誤！月份範圍限於 1~12")


# Date_function.py 測試程式
if __name__ == "__main__":
    # 測試預設情況 (空格參數 = 0，日期間不空格)
    print_date(1, 0)
    # 分隔線
    print("---------------------")
    # 測試 2 月自動判斷閏年印出情況 (空格參數使用預設值，省略)
    print_date(2)
    # 分隔線
    print("---------------------")
    # 測試輸入月份超出範圍情況 (空格參數使用預設值，省略)
    print_date(13)
