def add(number,number2):
    print("The sum =", number+number2)
def cube(number):
    print("Cube = ", number*number)
def max3(number,number2,number3):
    if number>number2 and number>number3:
        print("Number #1 is Greater!")
    elif number2>number and number2>number3:
        print("Number #2 is Greater!")
    elif number3>number and number3>number2:
        print("Number #3 is Greater!")

number=int(input("Enter value =>"))
number2=int(input("Enter value =>"))
number3=int(input("Enter value =>"))
add(number,number2)
cube(number)
max3(number,number2, number3)
