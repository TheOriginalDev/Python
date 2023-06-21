ce=0
co=0
se=0
so=0
sa=0
print("*"*86)
print("Count even, odd numbers, sum of even, sum of odd, and sum of all numbers in set range")
print("*"*86)
n=int(input("Enter Limit =>"))
for i in range(1,n+1):
    if i%2==0:
        ce=ce+1
        se=se+i
    else:
        co=co+1
        so=so+i
sa=so+se
print("The count of even numbers:",ce, "The count of odd numbers:", co)
print("The sum of even numbers:",se, "The sum of odd numbers:", so)
print("The sum of all numbers", sa)