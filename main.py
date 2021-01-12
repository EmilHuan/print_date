# 匯入 Date_function.py
import Date_function

# 主程式用 while True 包覆，出現例外 (Exception) 時可重新讓使用者輸入
while True:
    # 例外處理
    try:
        # while True 檢查的主程式，請使用者輸入月份、星期幾
        month = eval(input("請輸入月份 (1~12)："))
        week_number = eval(input("請輸入當月一號星期數字 (1~7):"))

        # 如月分 == 2 月，請使用者輸入潤月天數 (28 or 29)
        if month == 2:
            Feb_leap_or_not = eval(input("輸入二月天數 (28 或 29)："))
        # 如月份 != 2 月，天數參數一律定為預設的 28 天
        else:
            Feb_leap_or_not = 28

    # SyntaxError 例外，輸入值出現特殊字元時回傳錯誤訊息
    except SyntaxError:
        print("錯誤！輸入值不能有特殊字元，請重新輸入")
        print()
    # NameError 例外，輸入值出現文字時回傳錯誤訊息
    except NameError:
        print("錯誤！輸入值不能有文字，請重新輸入")
        print()

    # 如例外檢查通過，執行 Date_function.py 檔案裡的函數 print_date
    else:
        Date_function.print_date(month, week_number, Feb_leap_or_not)
        # 函數執行完畢後顯示感謝使用者的話
        print("感謝您的使用！")
        # 終止 while True
        break
