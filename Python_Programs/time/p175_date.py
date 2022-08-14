import datetime
y=int(input("Enter Year =>"))
m=int(input("Enter Month =>"))
d=int(input("Enter Day Of The Month =>"))
Date = datetime.datetime(y, m, d)
print(Date)