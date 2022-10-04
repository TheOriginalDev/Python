x = 0
c5 = 0
c10 = 0
while x <= 100:
    if x % 5 == 0:
        c5 = c5 + 1
    elif x % 10 == 0:
        c10 = c10 + 1
    x = x + 1
print("The numbers divisible by 5 =>", c5, "The numbers divisible by 10 =>", c10)
