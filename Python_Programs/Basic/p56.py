n=int(input("Enter limit ="))
ce=0
co=0
i=1
while i<=n:
    if i%2==0:
        ce=ce+1
    else:
        co=co+1
    i = i + 1
print("The count of even numbers =",co)
print("The count of odd numbers =", ce)