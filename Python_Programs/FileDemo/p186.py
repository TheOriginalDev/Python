f1 = open("abc", "r")
c=0
while True:
    data = f1.read(1)
    if not data:
        break
    if data=="a" or data=="e" or data=="i" or data=="o" or data=="u" or data=="A" or data=="E" or data=="I" or data=="O" or data=="U":
        print("7",end="")
    else:
        print(data,end="")


f1.close()
