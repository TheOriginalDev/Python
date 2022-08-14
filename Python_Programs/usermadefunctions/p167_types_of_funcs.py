def add(): # without argument and without return
    a=2
    b=2
    print("Add = ",a+b)
def addwr(x,y): # with argument and without return
    a=x
    b=y
    print("Add = ",a+b)
def addar(x,y): # with argument and with return
    return x+y
def addr(): # without argument and with return
    x=22
    y=33
    return x+y

add()
addwr(22,55)
ans=addar(5,6)
print(ans)
ans=addr()
print(ans)
