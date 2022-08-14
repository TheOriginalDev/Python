import random
n=int(input("Enter the amount of questions you want to be asked =>"))
for i in range (1,n+1):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print("Number_1 = ",x, "Number_2 =",y)
    add=int(input("Enter addition of this =>"))
    if x+y==add:
        print("Correct")
    else:
        print("Incorrect")