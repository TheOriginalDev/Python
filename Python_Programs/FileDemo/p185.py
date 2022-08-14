f1 = open("abc", "r")
while True:
    data = f1.read(1)
    if not data:
        break
    if data==" ":
        pass
    else:
        print(data,end="")
f1.close()