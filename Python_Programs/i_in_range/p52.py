ce=0
co=0
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    if i%2==0:
        ce=ce+1
    else:
        co=co+1

print("The number of even numbers =", ce)
print("The number of odd numbers =", co)