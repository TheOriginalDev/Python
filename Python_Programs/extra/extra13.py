limit=int(input("Enter limit =>"))
sum_even=0
sum_odd=0
even=0
odd=0
i=1
while i<=limit:
    if i%2==0:
        even=even+1
        sum_even=sum_even+i
    else:
        odd=odd+1
        sum_odd=sum_odd+i
    i=i+1
print("The sum of even numbers =>",sum_even)
print("The sum of odd numbers =>",sum_odd)