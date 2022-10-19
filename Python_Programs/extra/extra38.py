list1 = [5, 10, 8, 97, 6]
x = 0
sumofnumbers = 0
averagenumber = 0
while x < len(list1):
    sumofnumbers = sumofnumbers + list1[x]
    x = x + 1
averagenumber = sumofnumbers / len(list1)
print("The average of numbers =>", averagenumber)
print("Sum of Numbers =>", sumofnumbers + x)
