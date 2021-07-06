import datetime

# 印出系統年份
year = datetime.date.today().year
print(year)
print(type(year))

# 印出系統完整時間 (年、月、日、幾點幾分幾秒)
year2 = datetime.datetime.now()
print(year2)

# 印出今天是星期幾 (回傳數字 + 1 = 真的星期幾)
print(datetime.datetime.today().weekday())
# 印出今天是星期幾 (回傳數字 = 真的星期幾)
print(datetime.datetime.today().isoweekday())

# 功能不太確定
print(datetime.timedelta(days=1))

# 印出指定月份日曆
import calendar
cal = calendar.month(2015, 12)
print(cal)

# 回傳指定日期是星期幾
import datetime
day = datetime.datetime(2021, 7, 1)
print(day)
print(day.isoweekday())
print("星期%d" % (day.weekday() + 1))



