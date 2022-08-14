f1=open("abc","r")

while True:
    data=f1.read(1)
    if not data:
        break
    print(data)
    
f1.close()