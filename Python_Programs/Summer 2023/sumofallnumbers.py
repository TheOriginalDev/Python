sumofallnumbers=0
print("*"*37)
print("Sum of all numbers within set range")
print("*"*37)
n=int(input("Enter limit =>"))
for i in range(1, n+1):
    sumofallnumbers=sumofallnumbers+i
print("Sum of all numbers within range of",n,"is equal to", sumofallnumbers)