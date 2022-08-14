import time
print("This is printed immediately.")
a=float(input("Enter Snooze Time =>"))
time.sleep(a)
print("This is printed after ",a," seconds.")