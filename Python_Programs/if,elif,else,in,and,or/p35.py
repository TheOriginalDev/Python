math=int(input("Enter your grade for math:"))
english=int(input("Enter your grade for english:"))
science=int(input("Enter your grade for science:"))
total=math+english+science
print("Total = ",total)
if total>0 and total<=50:
    print("Your grade is in C range.")
elif total>50 and total<=100:
    print("Your grade is in B range.")
else:
    print("Your grade is in A+ range")