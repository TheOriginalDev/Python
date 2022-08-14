import time
current = time.localtime(time.time())
h=current.tm_hour

if h>0 and h<13:
    print("Good Morning!")
elif h>14 and h<19:
    print("Good Evening!")
elif h>15 and h<23:
    print("Good Night!")