list1 = [5, 10, 8, 97, 6]
x = 0
sumofnumbers = 0
averagenumber = 0
for x in range(0,5):
    if list1[x]%2==0:
        sumofnumbers=sumofnumbers+list1[x]
print("Sum of even numbers =>", sumofnumbers)