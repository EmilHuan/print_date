# test = tuple(i for i in range(1, 13))
# print(test)

week_number_tuple = tuple(i for i in range(1, 8))
month_tuple = tuple(i for i in range(1, 13))

print(week_number_tuple)
print(month_tuple)


# 測試印出空格 function
def blank_rows(number):
    number += 1
    for i in range(1, number):
        i += 1
        print("空格")


if __name__ == '__main__':
    # 測試 blank_rows() function
    blank_rows(3)
    print("----------")
    blank_rows(0)

