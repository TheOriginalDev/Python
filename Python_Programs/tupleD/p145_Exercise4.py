c=0
tupleD=(11,22,33,44,55,11,99,33)
for x in tupleD:
    if x%2==0:
        c=c+1
        print(x,"is even number")
print("The count of even numbers =>",c)
