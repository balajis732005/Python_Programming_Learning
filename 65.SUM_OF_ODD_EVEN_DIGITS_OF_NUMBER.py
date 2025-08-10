# SUM OF ODD and EVEN DIGITS OF NUMBER
num=int(input("Enter a number : "))
odd=0
even=0
for i in range(0,len(str(num))):
    rem=num%10
    if rem%2==0:
        even+=rem
    elif rem%2!=0:
        odd+=rem
    num//=10
print("SUM OF ODD DIGITS OF NUMBER : ",odd)
print("SUM OF EVEN DIGITS OF NUMBER : ",even)

        
