counter=0
list=[23,56,67,12,78,34,89,44,66,88,11,31,42,34]
for eachvalue in list:
    if eachvalue > 25:
        counter = counter+1
print("The count of numbers greater than 25 =>", counter)

s1={1,2,3,4,5,6}
s2={6,7,8,9}
print(s1&s2)