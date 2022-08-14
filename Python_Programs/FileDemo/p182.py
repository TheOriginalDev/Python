f1 = open("abc", "r")
c=0
while True:
    data = f1.read(1)
    if not data:
        break
    if data==" ":
        c=c+1
f1.close()
print("Total spaces =",c,"Total Words =",c+1)