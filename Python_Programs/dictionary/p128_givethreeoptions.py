import random

d1 = {}
n = int(input("Enter limit of students =>"))

for i in range(1, n + 1):
    k = random.randint(1, 40)
    v = random.randint(1, 30)
    d1[k] = v

print("Enter P to Display Only Pass Students =>")
print("Enter F to Display Only Fail Students =>")
print("Enter PF to Display Pass & Fail Students =>")
op=(input("Enter Option =>"))

if op=="P":

    print("ID\t\tResult\t\tRollno\t\tMarks")
    print("*"*40)
    for key,value in d1.items():
        if value>18:
            print(i,"\t\t" "PASS","\t\t",key,"\t\t",value)

    print("*"*40)

elif op=="F":
    print("ID\t\tResult\t\tRollno\t\tMarks")
    print("*" * 40)
    for key, value in d1.items():
        if value <18:
            print(i, "\t\t" "FAIL", "\t\t", key, "\t\t", value)

    print("*" * 40)

elif op=="PF":
    print("ID\t\tResult\t\tRollno\t\tMarks")
    print("*" * 40)
    for key, value in d1.items():
        if value > 18:
            print(i, "\t\t" "PASS", "\t\t", key, "\t\t", value)
        else:
            print(i, "\t\t" "FAIL", "\t\t", key, "\t\t", value)

    print("*" * 40)