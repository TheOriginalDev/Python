number1 = int(input("Enter a number"))
number2 = int(input("Enter a number"))
number3 = int(input("Enter a number"))
if number1>number2 and number1>number3:
    print("number 1 is greater!")
elif number2>number1 and number2>number3:
    print("number 2 is greater")
elif number3>number1 and number3>number2:
    print("number 3 is greater")
else:
    print("All are equal!")