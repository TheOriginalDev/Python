f1 = open("abc", "r")
u=0
l=0
while True:
    data = f1.read(1)
    if not data:
        break
    if data.isupper():
        print(data.lower(),end="")
    elif data.islower():
        print(data.upper(),end="")
    else:
        print(data,end="")

f1.close()