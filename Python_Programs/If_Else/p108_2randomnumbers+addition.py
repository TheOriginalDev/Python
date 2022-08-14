import random
x=random.randint(1,50)
y=random.randint(1,50)
print("Number_1 = ",x, "Number_2 =",y)
add=int(input("Enter addition of this =>"))
if x+y==add:
    print("Yes, you are correct!")
else:
    print("Sorry, better luck next time!")