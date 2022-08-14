print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")
op=input("Enter option =>")
if op=="+":
    number=float(input("Enter a random number:"))
    number2=float(input("Enter a random number:"))
    addition=number+number2
    print("The value =",addition)
elif op=="-":
    number = float(input("Enter a random number:"))
    number2 = float(input("Enter a smaller number:"))
    subtraction = number-number2
    print("The value =",subtraction)
elif op=="*":
    number = float(input("Enter a random number:"))
    number2 = float(input("Enter a random number:"))
    multiplication = number * number2
    print("The value =",multiplication)
elif op=="/":
    number = float(input("Enter a random number:"))
    number2 = float(input("Enter a smaller number:"))
    division = number / number2
    print("The value =",division)
else:
    print("Wrong option")