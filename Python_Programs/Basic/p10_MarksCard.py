English=float(input("Enter Marks For English="))
Math=float(input("Enter Marks for Math="))
Science=float(input("Enter Marks for Science="))
TotalScore=English+Math+Science
print("The Total Score =",TotalScore)
if TotalScore>50:
    print("Success! You passed, go out and Celebrate with your parents!")
else:
    print("You failed, try again next and go call your parents :'(")