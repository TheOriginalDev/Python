list1=[11,22,11,44,55,66,88,22]
list2=[]
for x in list1:
    if x%2==0:
        list2.append(x)

for x in list2:
    if x in list1:
        list1.remove(x)

print(list1)