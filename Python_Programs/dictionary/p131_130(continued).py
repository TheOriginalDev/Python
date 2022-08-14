d1 = {1: [2, 3, 4], 22: [11, 22, 33], 34: [5, 6, 7], 41: [34, 22, 34], 7: [56, 18, 24], 8: [29, 43, 57],
      59: [18, 26, 33]}
z=int(input("Enter Roll Number =>"))
print("no\tEng\tHin\tSS\tTotal")
print("*"*50)
no=1
for key,value in d1.items():
    if key==z:
        m1,m2,m3=value
        total=sum(value)
        if total>18:
            print(key,"\t\t",m1,"\t\t",m2,"\t\t",m3,"\t\t","PASS")
        else:
            print(key, "\t\t", m1, "\t\t", m2, "\t\t", m3, "\t\t", "FAIL")
        no=no+1
print("*"*50)

if no==1:
    print("Sorry not found")