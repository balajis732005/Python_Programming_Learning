# To check whether the given number is palindrome or not
num=int(input("Enter a number : "))
rev=0
temp_num=num
for i in range(0,len(str(num))): #we can use both while loop and for loop
#while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10
print("REVERSED NUMBER : ",rev)
if temp_num==rev:
    print(temp_num," is an PALINDROME NUMBER")
else:
    print(temp_num," is not an PALINDROME NUMBER")
print("\nREVERSE A NUMBER BY USING STRING SLICING : \n")
print("REVERSED NUMBER : ",str(temp_num)[::-1])

    
