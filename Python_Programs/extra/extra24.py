number = int(input("Enter Number =>"))
s=0


for i in range(1,number + 1):
    if i%2==0:
        print("+",i,end="")
        s=s+i
    else:
        print("-",i,end="")
        s=s-i
print("\nsum = ",s)