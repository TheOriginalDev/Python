number = int(input("Enter Number =>"))
s=0


for i in range(1,number + 1):

    if i % 2 == 0:
        print(i*i,"+ ",end="")
        s=s+i*i
    else:
        print(i*i*i,"+ ",end="")
        s=s+i*i*i
print("\nProduct = ",s)