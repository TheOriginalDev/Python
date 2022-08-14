print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
op=int(input("Enter option =>"))
if op==1:
    number=float(input("Enter a random number:"))
    number2=float(input("Enter a random number:"))
    addition=number+number2
    print("The value =",addition)
elif op==2:
    number = float(input("Enter a random number:"))
    number2 = float(input("Enter a smaller number:"))
    subtraction = number-number2
    print("The value =",subtraction)
elif op==3:
    number = float(input("Enter a random number:"))
    number2 = float(input("Enter a random number:"))
    multiplication = number * number2
    print("The value =",multiplication)
elif op==4:
    number = float(input("Enter a random number:"))
    number2 = float(input("Enter a smaller number:"))
    division = number / number2
    print("The value =",division)
else:
    print("Wrong option")