# To find whether the given number is armstrong number or not
'''
EXAMPLE : 153 (digit=3)
1**3 =   1
5**3=125
3**3=  27  (+)
------------
         153
------------
'''
num=int(input("Enter a number : "))
temp_num=num
add=0
length=len(str(num))
for i in range(0,length):
    rem=num%10
    add+=(rem**length)
    num//=10
if add==temp_num:
    print(temp_num," is an ARMSTRONG NUMBER")
else:
     print(temp_num,"is NOT an ARMSTRONG NUMBER")
