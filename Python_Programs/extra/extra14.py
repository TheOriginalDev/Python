i=0
ce=0
co=0
list=[23,56,67,12,78,34,89,44,66,88,11,31,42,34]
print(len(list))
while i<len(list):
    if list[i]%2==0:
        ce=ce+1
    else:
        co=co+1
    i=i+1