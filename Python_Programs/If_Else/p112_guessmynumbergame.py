import random
x=random.randint(1,30)
y=0
t=0
while x!=y:
    y=int(input("Guess my number ;) =>"))
    if x>y:
        print("Plz think higher value! ;)")
    elif x<y:
        print("Plz think lower value! ;)")
    t=t+1

print("WINNER! WINNER! :D You tried",t,"times!")
