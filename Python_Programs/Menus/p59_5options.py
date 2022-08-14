while True:
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")
    print("Enter 5 for exit")
    op=int(input("Enter option =>"))

    if op==1:
        n=float(input("Enter number:"))
        s=float(input("Enter another number:"))
        print("The sum of the two numbers =>", n+s)
    elif op==2:
        n = float(input("Enter number:"))
        s = float(input("Enter another number:"))
        print("The subtraction of the two numbers =>", n-s)
    elif op==3:
        n=float(input("Enter number:"))
        s=float(input("Enter another number:"))
        print("The multiplication of the two numbers =>", n*s)
    elif op==4:
        n = float(input("Enter number:"))
        s = float(input("Enter another number:"))
        print("The division of the two numbers =>", n/s)
    elif op==5:
        break
    else:
        print("Wrong option, enter options 1-5")

