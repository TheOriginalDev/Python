print("Enter s for square")
print("Enter c for cube")
op=input("Enter option =>")

if op=="s" or op=="S":
    number=int(input("Enter a random number:"))
    square=number*number
    print("The square value = ",square)
elif op=="c" or op=="C":
    number = int(input("Enter a random number:"))
    cube=number*number*number
    print("The cube value = ",cube)

else:
    print("Wrong option")