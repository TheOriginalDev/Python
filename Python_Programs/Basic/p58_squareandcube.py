
while True:
    print("Enter 1 to square number")
    print("Enter 2 to cube number")
    print("Enter 3 for exit")
    op=int(input("Enter option =>"))

    if op==1:
        n = int(input("Enter number =>"))
        print("The number squared = ",n*n)
    elif op==2:
        n = int(input("Enter number =>"))
        print("The number cubed = ",n*n*n)
    elif op==3:
        break
    else:
        print("Wrong option, enter 1,2,or 3")