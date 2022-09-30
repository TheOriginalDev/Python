number = int(input("Enter Number =>"))
s=0


for i in range(1,number + 1):
    print(i*i,"+", end="")
    s=s+i*i

print("\nProduct = ",s)