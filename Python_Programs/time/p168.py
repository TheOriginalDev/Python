import time
current = time.localtime(time.time())
print("Year:", current.tm_year)
print("Month:", current.tm_mon)
print("Day:", current.tm_mday)
print("Weekday:", current.tm_wday)
print("Yearday:", current.tm_yday)
h= current.tm_hour
m=current.tm_min
s=current.tm_sec
print("Hour:", current.tm_hour)
print("Minutes:", current.tm_min)
print("Seconds:", current.tm_sec)

print("The Time Currently is:",h,":",m,":",s)