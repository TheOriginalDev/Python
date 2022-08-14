import random
x=random.randint(1,30)
print(x)
y=0
t=0
s=1
e=30
while x!=y:
    print("Your range is ",s," -- ",e)
    y=int(input("Guess my number ;) =>"))
    if x>y:
        print("Plz think higher value! ;)")
        s=y
    elif x<y:
        print("Plz think lower value! ;)")
        e=y
    t=t+1

print("WINNER! WINNER! :D You tried",t,"times!")
