limit=int(input("Enter limit =>"))
even=0
odd=0
i=1
while i<=limit:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("The amount of even numbers =>", even,"The amount of odd numbers =>",odd)