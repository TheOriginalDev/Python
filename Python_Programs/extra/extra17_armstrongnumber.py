x=int(input("Enter number =>"))
no=x
i=0
rev=0
"number=567"


while x>0:
    rem=x%10 #1. 7, 2. 6, 3. 5
    rev=rev+rem**3 #1. 7, 2. 76, 3. 765
    x=x//10 #1. 56, 2. 5, 3. 0


print("Reverse no = ",rev," X = ",no)


if rev==no:
    print("It's Armstrong Number!")
else:
    print("It's not Armstrong number!")
