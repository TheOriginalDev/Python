n=input("Enter number: ")
temp=int(n)
sum=0
a=len(n)
while temp!=0: d=temp%10
sum=sum+(d**a)
temp=temp//10
if(sum==int(n)):
    print("Number is armstrong.")
else:
    print("Number is not armstrong.")