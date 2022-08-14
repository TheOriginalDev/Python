f1 = open("abc", "r")
u=0
l=0
while True:
    data = f1.read(1)
    if not data:
        break
    if data.isupper():
        u=u+1
    elif data.islower():
       l=l+1

print("Uppercase Letters =>",u,"Lowercase Letters =>",l)