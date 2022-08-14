print("Enter 1 for square")
print("Enter 2 for cube")
print("Enter 3 for addition")
op=int(input("Enter option =>"))

if op==1:
    number=int(input("Enter a random number:"))
    square=number*number
    print("The square value = ",square)
elif op==2:
    number = int(input("Enter a random number:"))
    cube=number*number*number
    print("The cube value = ",cube)
elif op==3:
    number=int(input("Enter a random number:"))
    number1=int(input("Enter another random number:"))
    addition=number+number1
    print("The addition value =", addition)

else:
    print("Wrong option")