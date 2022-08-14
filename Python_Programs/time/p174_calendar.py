import calendar
y=int(input("Enter Current Year =>"))
m=int(input("Enter Current Month =>"))
cal = calendar.month(y, m)
print(cal)