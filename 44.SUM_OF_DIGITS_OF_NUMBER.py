# To find the sum of all digits and first,last digits of a given number
num=int(input("Enter a number : "))
add=0
temp_num=num
for i in range(0,len(str(num))):
    rem=num%10
    add+=rem
    num//=10
print("SUM OF ALL DIGITS OF YOUR NUMBER ",temp_num," is : ",add)
temp2_num=temp_num
last=temp_num%10
for i in range(0,len(str(temp_num))-1):
    temp_num//=10
    first=temp_num
print("SUM OF FIRST AND LAST DIGITS OF YOUR NUMBER ",temp2_num," is : ",last+first) 
    
