print("Enter 1 for Positive or Negative")
print("Enter 2 for Odd or Even")
print("Enter 3 for Area of Triangle")
print("Enter 4 for Maximum value out of 2")
op=int(input("Enter option =>"))
if op==1:
    number=float(input("Enter number =>"))
    if number>0:
        print(number,"It is positive")
    elif number<0:
        print("It is negative",number)
    else:
        print("Number is neutral (0)")
elif op==2:
    number=int(input("Enter number =>"))
    if number==0:
        print("Neutral")
    elif number%2==0:
        print("This number is an even one!")
    else:
        print("Number is odd")
elif op==3:
    h=float(input("Enter height =>"))
    b=float(input("Enter base =>"))
    print("Area of triangle = ",h*b*0.5)
elif op==4:
    a=float(input("Enter first number =>"))
    b=float(input("Enter second Number =>"))
    if a>b:
        print("The first number is greater! ")
    else:
        print("The second number is greater")
else:
    print("Please enter options between 1-4.")

