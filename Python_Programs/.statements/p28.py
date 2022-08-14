letter=input("Enter any letter =>")

print(letter.isdigit())
print(letter.isdecimal())
print(letter.isupper())
print(letter.islower())

if letter.islower():
    print(letter.upper())
elif letter.isupper():
    print(letter.lower())