### 印出近三個月日期
# 匯入 Date_function.py
import Date_function
# new computer git test

# 計算執行次數
count = 0

# 主程式用 while True 包覆，出現例外 (Exception) 時可重新讓使用者輸入
while True:
    # 例外處理
    try:
        # 每次執行後 +1
        count += 1
        
        # 如為第一次執行，則直接帶入當前月份 & 空一行
        if count == 1:
            month = Date_function.now_month()
            blank_number = 1
        # 第二次開始，皆詢問月份 & 空行數 (while true 最多循環 100 次)
        elif count <= 100:
            # while True 檢查的主程式，請使用者輸入月份、星期幾、日期間要空幾行
            month = eval(input("請輸入月份 (1~12)："))
            # blank_number_chr 先不轉換成數字，且去掉左右兩側空格
            blank_number_chr = (input("請輸入每個日期間的空行數 (不輸入則使用預設值空一行)：")).strip()

            # 如輸入 blank_number_chr 時直接按 Enter，則 blank_number == 1 (預設空一行)
            if blank_number_chr == "":
                blank_number = 1
            # 如有輸入，則轉換為數字並當作 blank_number 的變數值 (自訂空幾行)
            else:
                blank_number = eval(blank_number_chr)
        # 避免 while true 無限循環，count > 100 後中止程式
        else:
            break

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
        # 一次印出一季 (三個月) 的日期
        for i in range(3):
            Date_function.print_date(month + i, blank_number)
        
        print()
        # 詢問使用者是否要繼續列印其它月份
        next_print = input("要再列印其它月份嗎？(繼續列印請輸入 y，結束列印請按任意鍵)：")
        if next_print.lower() == "y":
            pass
            print(count)
        else:
            # 函數執行完畢後顯示感謝使用者的話
            print("感謝您的使用！")
            # 終止 while True (結束列印)
            break

            
