import random
d1={}
n=int(input("Enter limit of students =>"))
z=int(input("Enter Rollno =>"))

for i in range(1,n+1):
    k=i
    print(k)
    v=random.randint(1,30)
    print(v)
    d1[k]=v

print(d1) #correct?

i=1
for key,value in d1.items():
    if key==z:
        print("ID\t\tResult\t\tRollno\t\tMarks")
        print("*" * 40)
        print(i,"\t\t" "PASS","\t\t",key,"\t\t",value)
        i=i+1
        print("*"*40)

if i==1:
    print("Sorry not found")