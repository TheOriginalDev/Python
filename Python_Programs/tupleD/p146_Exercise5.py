c=0
tupleD=(11,22,33,44,49,55,11,99,33)
for x in tupleD:
    if x%7==0:
        c=c+1
print(sum(tupleD))
print("The count of numbers divisible by 7 =>", c)
