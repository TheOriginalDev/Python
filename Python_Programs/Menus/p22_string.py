print("Enter p for Positive or Negative")
print("Enter o for Odd or Even")
print("Enter area for Area of Triangle")
print("Enter m for Maximum value out of 2")
op = input("Enter option =>")
if op == "p":
    number = float(input("Enter number =>"))
    if number > 0:
        print(number, "It is positive")
    elif number < 0:
        print("It is negative", number)
    else:
        print("Number is neutral (0)")
elif op == "o":
    number = int(input("Enter number =>"))
    if number == 0:
        print("")
    elif number % 2 == 0:
        print("This number is an even one!")
    else:
        print("Number is odd")
elif op == "area":
    h = float(input("Enter height =>"))
    b = float(input("Enter base =>"))
    print("Area of triangle = ", h * b * 0.5)
elif op == "m":
    a = float(input("Enter first number =>"))
    b = float(input("Enter second Number =>"))
    if a > b:
        print("The first number is greater! ")
    elif b>a:
        print("The second number is greater")
    else:
        print("Both are equal")
else:
    print("Please enter options between 1-4.")

