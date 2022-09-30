ce=0
co=0
for i in range(1, 101):
    if i % 2 == 0:
        ce = ce+1
    else:
        co = co+1

print("The number of even numbers =>", ce, "The amount of odd numbers =>", co)
