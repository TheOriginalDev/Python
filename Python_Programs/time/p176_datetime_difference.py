import datetime
today = datetime.date.today()
y=int(input("Enter Birth Year =>"))
m=int(input("Enter Birth Month =>"))
d=int(input("Enter Day Of Birth =>"))
birthDate = datetime.date(y,m,d)
age = today.year - birthDate.year
print(age)