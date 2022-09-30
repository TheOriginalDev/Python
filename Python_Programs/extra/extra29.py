numbers=[23, 45, 67, 89, 11, 44, 66, 678, 899, 234, 5677]
ce=0
co=0
for i in range(1,len(numbers)):
    if numbers[i]%2==0:
        ce=ce+1
    else:
        co=co+1
print("The even numbers =>",ce,"The odd numbers =>",co)
