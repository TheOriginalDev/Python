import random
n=int(input("Enter the amount of questions you want to be asked =>"))
op=(input("Enter the operation you want to solve =>"))
if op=="-":
    cr = 0
    cw = 0
    for i in range(1, n + 1):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        print("Number_1 = ", x, "Number_2 =", y)
        sub = int(input("Enter subtraction of this =>"))
        if x-y==sub:
            cr = cr+ 1
            print("Correct")
        else:
            cw=cw+1
            print("Incorrect")
    print("The amount of times correct =>", cr, "The amount of times wrong =>", cw)

elif op=="+":
    cr = 0
    cw = 0
    for i in range (1,n+1):
        x=random.randint(1,50)
        y=random.randint(1,50)
        print("Number_1 = ",x, "Number_2 =",y)
        add=int(input("Enter addition of this =>"))
        if x+y==add:
            cr=cr+1
            print("Correct")
        else:
            cw=cw+1
            print("Incorrect")
    print("The amount of times correct =>",cr,"The amount of times wrong =>",cw)
elif op=="*":
    cr = 0
    cw = 0
    for i in range(1, n + 1):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        print("Number_1 = ", x, "Number_2 =", y)
        mult=int(input("Enter multiplication of this =>"))
        if x*y==mult:
            cr = cr + 1
            print("Correct")
        else:
            cw = cw + 1
            print("Incorrect")
    print("The amount of times correct =>", cr, "The amount of times wrong =>", cw)

elif op=="/":
    cr = 0
    cw = 0
    for i in range(1, n + 1):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        print("Number_1 = ", x, "Number_2 =", y)
        div=int(input("Enter division of this =>"))
        if x/y == div:
            cr = cr + 1
            print("Correct")
        else:
            cw = cw + 1
            print("Incorrect")
    print("The amount of times correct =>", cr, "The amount of times wrong =>", cw)


else:
    print("wrong option")
