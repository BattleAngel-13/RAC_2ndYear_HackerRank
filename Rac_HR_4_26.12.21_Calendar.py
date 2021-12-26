import calendar
month, date, year = map(int, input().strip().split())
a = calendar.day_name[calendar.weekday(year, month, date)].upper()
print(a)
