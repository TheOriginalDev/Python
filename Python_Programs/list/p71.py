numbers=[12,18,-5,-7,23,2010,-23,-45,23]
c=0
s=0

for x in numbers:
    if x%7==0:
        print(x,"is divisible by 7")
        c=c+1
        s=s+x

print("The sum of numbers = ",s)
print("The count of numbers =", c)