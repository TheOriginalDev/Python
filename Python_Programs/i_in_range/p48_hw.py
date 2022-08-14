n=int(input("Enter limit =>"))
m=1
for i in range(1,n+1):
    print(i," X ",end="")
    m=m*i

print("\nFact = ",m)
