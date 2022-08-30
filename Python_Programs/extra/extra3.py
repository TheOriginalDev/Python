odd = 0
even = 0
evensum=0
oddsum=0
limit = int(input("Enter limit of numbers =>"))
for eachvalue in range(1, limit+1):
    if eachvalue % 2 == 0:
        even = even + 1
        evensum = eachvalue + evensum
    else:
        odd = odd + 1
        oddsum = eachvalue + oddsum
print("Even Numbers =>", even, "\n" "Odd Numbers =>", odd, "\n" "Total of Even Numbers =>", evensum, "\n" "Total of Odd Numbers =>", oddsum, "\n" "Total of Even and Odd numbers =>", evensum+oddsum)