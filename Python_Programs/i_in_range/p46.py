n=int(input("Enter limit=>"))
c1=0
s1=0
for i in range(1,n+1):
    if i%7==0:
        print(i,"It is divisible by 7")
        c1=c1+1
        s1=s1+i

print("Sum of numbers divisible by 7:",s1)
print("Count of numbers divisible by 7:",c1)