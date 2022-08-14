import time
current = time.localtime(time.time())
year=current.tm_year
if year%4==0:
    print("It is a leap year!")
else:
    print("It is not a leap year!")