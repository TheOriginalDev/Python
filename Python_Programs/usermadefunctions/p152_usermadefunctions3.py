def add():
    b1 = int(input("Enter Number #1 =>"))
    b2 = int(input("Enter Number #2 =>"))
    print("The sum =", b1 + b2)
def cube():
    a = int(input("Enter no =>"))
    print("Cube = ", a * a)
def max3():
    n1 = int(input("Enter Number #1 =>"))
    n2 = int(input("Enter Number #2 =>"))
    n3 = int(input("Enter Number #3 =>"))
    if n1>n2 and n1>n3:
        print("Number #1 is Greater!")
    elif n2>n1 and n2>n3:
        print("Number #2 is Greater!")
    elif n3>n1 and n3>n2:
        print("Number #3 is Greater!")


add()
cube()
max3()
