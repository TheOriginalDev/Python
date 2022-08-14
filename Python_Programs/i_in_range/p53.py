counter=0
n=int(input("Enter number which is a factor of 5 =>"))
for i in range(1,n+1):
    if i%5==0:
        counter=counter+1

print("The number of multiples of 5 in",n,"=>",counter)