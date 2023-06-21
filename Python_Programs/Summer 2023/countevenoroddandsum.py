# breakpoint()
# (Pdb)
# Now you can apply different commands, e.g., print variables/expressions or execute the script line by line. The most useful commans are listed below. For a full list have a look at the official documentation here.

# h (elp): Print the list of available commands
# l (ist): List source code for the current file
# w (here): Print a stack trace, with the most recent frame at the bottom
# q (uit): Quit from the debugger
# p expression: Evaluate the expression in the current context and print its value
# n (ext): Continue execution until the next line in the current function is reached or it returns (The difference between next and step is that step stops inside a called function, while next executes called functions, only stopping at the next line in the current function)
# s (tep): Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function)
# c (ontinue): Continue execution, only stop when a breakpoint is encountered

ce = 0
co = 0
se = 0
so = 0
sa = 0
listeven = []
listodd = []
print("*" * 86)
print("Count even, odd numbers, sum of even, sum of odd, and sum of all numbers in the set of range")
breakpoint()
print("*" * 86)
n = int(input("Enter your Limit/Range =>"))
for i in range(1, n + 1):
    if i % 2 == 0:
        ce = ce + 1
        se = se + i
        listeven.append(i)
    else:
        co = co + 1
        so = so + i
        listodd.append(i)
sa = so + se
print("The list of even numbers are =>", listeven)
print("The count of even numbers:", ce)
print("The list of odd numbers are =>", listodd)
print("The count of odd numbers:", co)
print("The sum of even numbers:", se)
print("The sum of odd numbers:", so)
print("The sum of all numbers", sa)
