name=input("Please Enter Your Name =>")
claSS=int(input("Please Enter Your Class =>"))
city=str(input("Please Enter Your City You Live In =>"))
percentage=int(input("Please Enter your Percentage =>"))
if 80 < percentage < 100:
    print("A Grade!")
elif 65 < percentage < 79:
    print("B Grade!")
elif 50 < percentage < 64:
    print("C Grade!")
elif 40 < percentage < 49:
    print("D Grade!")
elif percentage<40:
    print("E Grade!")
