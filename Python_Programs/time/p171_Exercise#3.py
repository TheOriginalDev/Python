import time
current = time.localtime(time.time())
h=current.tm_hour

if h>0 and h<12:
    print("AM")
elif h>13 and h<23:
    print("PM")