import random
d1={}
n=int(input("Enter limit of students =>"))
p=0
f=0
for i in range(1,n+1):
    k=random.randint(1,40)
    v=random.randint(1,30)
    d1[k]=v

print("ID\t\tResult\t\tRollno\t\tMarks")
print("*"*40)
i=1
for key,value in d1.items():
    if value>18:
        p=p+1
        print(i,"\t\t" "PASS","\t\t",key,"\t\t",value,"\t\t",p)
    else:
        f=f+1
        print(i,"\t\t" "FAIL","\t\t",key,"\t\t",value,"\t\t",f)
    i=i+1

print("*"*40)