def areaoftriangle():
    h= int(input("Enter height =>"))
    b= int(input("Enter base =>"))
    print("Area of traingle = ",h*b*0.5)

def cube():
    a=int(input("Enter no =>"))
    print("Cube = ",a*a)

def table():
    n = int(input("Enter Limit ="))
    m = int(input("Enter limit for table ="))
    i = 1
    while i <= m:
        print(n, "X", i, "=", n * i)
        i = i + 1

def oddeven():
    n=int(input("Enter random number =>"))
    if n%2==0:
        print("Even")
    else:
        print("Odd")

def max2():
    n1=int(input("Enter Number #1 =>"))
    n2=int(input("Enter Number #2 =>"))
    if n1>n2:
        print("Number #1 is Greater!")
    elif n2>n1:
        print("Number #2 is Greater!")

def add():
    b1 = int(input("Enter Number #1 =>"))
    b2 = int(input("Enter Number #2 =>"))
    print("The sum =", b1+b2)

def positive_negative():
    l=int(input("Enter Number =>"))
    if l>0:
        print("You have a positive number!")
    else:
        print("You have a negative number!")

def areaofcircle():
    r=int(input("Enter Radius of Circle =>"))
    AOC=(3.14*r*r)
    print(AOC)

def factorial():
    f=1
    n=int(input("Enter any number =>"))
    for i in range(1,n+1):
        f=f*i
        print(i,"X",end="")
    print("\nFct = ",f)

def leapyear():
    year=int(input("Enter Year =>"))
    if year%4==0:
        print("It is a leap year!")
    else:
        print("It is not a leap year!")

areaoftriangle()
cube()
table()
oddeven()
max2()
add()
positive_negative()
areaofcircle()
factorial()
leapyear()
