List=[11,44,500,22,99,77,200,66,2,11,22]
List2=[]
x=int(input("Enter Value =>"))
for i in List:
    if i>x:
        List2.append(i)

print(List2)