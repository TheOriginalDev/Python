age=int(input("Enter age =>"))
if age < 18:
    print("You are minor and not eligible to vote.")
elif 18 <= age <= 60:
    print("You are young and eligible to vote.")
elif age > 60:
    print("You are a se19nior citizen person given special care to vote.")