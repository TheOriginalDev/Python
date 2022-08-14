import random
list1=[]
v=int(input("How many values do you want in list? =>"))
for i in range(1,v+1):
    value=random.randint(1,40)
    list1.append(value)

print(list1)
