# 判斷是否為閏年，如果是平年則回報最接近的閏年年份'

def leap_year():
    year = eval(input("請輸入一個年份："))

    if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)):
        print("您輸入的年份為「閏年」")
    else:
        print("您輸入的年份為「平年」")
        plusyear = year
        while (plusyear%4 != 0) or ((plusyear%400 != 0) and (plusyear%100 == 0)):
            plusyear += 1
        else:
            minusyear = year
            while (minusyear%4 != 0) or ((minusyear%400 != 0) and (minusyear%100 == 0)):
                minusyear -= 1
            else:
                if (plusyear - year) < (year - minusyear):
                    print("最接近您輸入年份的閏年為：{} 年".format(plusyear))
                elif (plusyear - year) > (year - minusyear):
                    print("最接近您輸入年份的閏年為：{} 年".format(minusyear))
                else:
                    print("最接近您輸入年份的閏年為：{} 及 {} 年".format(minusyear, plusyear))


# 測試程式
if __name__ == "__main__":
    leap_year()

