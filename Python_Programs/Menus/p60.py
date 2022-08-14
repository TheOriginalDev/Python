while True:
    print("Enter + for addition")
    print("Enter - for subtraction")
    print("Enter * for multiplication")
    print("Enter / for division")
    print("Enter e for exit")
    op=input("Enter option =>")

    if op=="+":
        n=float(input("Enter number:"))
        s=float(input("Enter another number:"))
        print("The sum of the two numbers =>", n+s)
    elif op=="-":
        n = float(input("Enter number:"))
        s = float(input("Enter another number:"))
        print("The subtraction of the two numbers =>", n-s)
    elif op=="*":
        n=float(input("Enter number:"))
        s=float(input("Enter another number:"))
        print("The multiplication of the two numbers =>", n*s)
    elif op=="/":
        n = float(input("Enter number:"))
        s = float(input("Enter another number:"))
        print("The division of the two numbers =>", n/s)
    elif op=="e":
        break
    else:
        print("Wrong option, enter options 1-5")

