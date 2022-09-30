list1=[20, 40, 60, 80, 20, 40, 20]
list2=[10, 50, 60, 70, 80, 90, 20, 50, 50]


ln1=(list1[-1])
ln1_1=(list1[0])


ln2=list2[-1]
ln2_1=list2[0]

if ln1==ln1_1 and ln2==ln2_1:
    print("list 1 =>",list1,"\n","The first and last number are the same!","\n","List 2 =>",list2,"\n","The first and last number are the same!")
else:
    print("not equal")

