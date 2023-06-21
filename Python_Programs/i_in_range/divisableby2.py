print("*" * 30)
print("Check if a number is divisible by 2")
print("*" * 30)
number = int(input("Enter limit =>"))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, "is even")
