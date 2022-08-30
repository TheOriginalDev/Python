number = int(input("Enter a number =>"))
remainder = number % 10
tens = number//10
sumOfDigits = remainder+tens
productOfDigits = remainder*tens
print("Sum of Digits =>", sumOfDigits)
print("Product of Digits =>", productOfDigits)
print("Sum of the Sum of Digits & Product of Digits =>", (sumOfDigits) + (productOfDigits))
if number == (sumOfDigits)+(productOfDigits):
    print("This is a special 2-digit number!")
else:
    print("It is not a special 2-digit number!")
