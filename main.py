# 匯入 Date_function.py
import Date_function

# 主程式用 while True 包覆，出現例外 (Exception) 時可重新讓使用者輸入
while True:
    # 例外處理
    try:
        # while True 檢查的主程式，請使用者輸入月份、星期幾、日期間要空幾行
        month = eval(input("請輸入月份 (1~12)："))
        week_number = eval(input("請輸入當月一號星期數字 (1~7):"))
        # blank_number_chr 先不轉換成數字，且去掉左右兩側空格
        blank_number_chr = (input("請輸入每個日期間的空行數 (不輸入則使用預設值空一行)：")).strip()

        # 如輸入 blank_number_chr 時直接按 Enter，則 blank_number == 1 (預設空一行)
        if blank_number_chr == "":
            blank_number = 1
        # 如有輸入，則轉換為數字並當作 blank_number 的變數值 (自訂空幾行)
        else:
            blank_number = eval(blank_number_chr)

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
        Date_function.print_date(month, week_number, blank_number)
        # 函數執行完畢後顯示感謝使用者的話
        print("感謝您的使用！")
        # 終止 while True
        break



