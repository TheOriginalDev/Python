n=int(input("Enter limit =>"))
c1=0
c2=0
s1=0
s2=0
for i in range(1,n+1):
    if i%2 ==0 :
        print(i," is even")
        c1=c1+1
        s1=s1+i
    else:
        print(i," is odd")
        c2=c2+1
        s2=s2+i

print("Count of odd =",c2," Count of even = ",c1)
print("Sum of odd = ",s2," Sum of even = ",s1)