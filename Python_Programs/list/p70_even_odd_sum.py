numbers=[12,18,-5,-7,23,2010,-23,-45,23]
e=0
o=0
se=0
so=0
for x in numbers:
    if x%2==0:
        e=e+1
        print(x,"is even")
        se=se+x
    else:
        o=o+1
        print(x,"is odd")
        so=so+x
print(numbers)
print("Total even values =",e," and sum of it",se)
print("Total odd values =",o,"and sum of it",so)