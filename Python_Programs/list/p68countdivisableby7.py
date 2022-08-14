numbers=[12,18,-5,-7,21,2010,-23,-45,23]
c=0
for x in numbers:
    if x%7==0:
        c=c+1
        print(x)
print("The amount of numbers divisible by 7 is:",c)