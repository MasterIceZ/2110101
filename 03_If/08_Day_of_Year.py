month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

def isLeapYear(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def day_of_year(d, m, y):
    if isLeapYear(y - 543):
        month_days[1] += 1
    days = d
    for i in range(0, m-1, 1):
        days += month_days[i]
    return days

print(day_of_year(int(input()), int(input()), int(input())))
