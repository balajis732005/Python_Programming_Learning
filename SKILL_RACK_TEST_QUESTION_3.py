'''
The integer numbers are passed as input.The program must print the number is multiple of sum of tenth and unit digit of number in reverse order .
if sum of unit and tenth digit is 0 then print that number otherwise print 0.
INPUT1:
702 402 502 702
OUTPUT1:
702 502 402 702
INPUT2:
344 707 342 505 500
OUTPUT2:
500 505 342 344
INPUT3:
403 507
OUTPUT3:
0
'''
num=list(map(int,input("Enter the input : ").split()))
print("OUTPUT : ",end="")
for i in range(-1,-(len(num))-1,-1):
    unit=num[i]%10
    ten=num[i]%100
    ten1=ten-unit
    ten2=ten1//10
    add=unit+ten2
    if add==0:
        print(num[i],end=" ")
    elif num[i]%add==0:
        print(num[i],end=" ")
    else:
        print(0)
