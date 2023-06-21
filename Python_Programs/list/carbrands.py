i=0
counter=0
carbrand=input("Enter the car brand you want to find =>")
list1=["Honda, Honda, Toyota, Maserati, Maserati, Maserati, BMW, Mercedes Benz, Toyota, Toyota, Toyota, Subaru, "
       "Subaru, Subaru"]
for x in list1:
    if x==carbrand:
        counter=counter+1
    else:
        print("Please Enter one of the following options =>"
              "Honda, Toyota, Maserati, BMW, Mercedes Benz, Subaru")
print("The number of times", carbrand, "popped up is =>", counter)