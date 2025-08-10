# To find the factorial of an number
num=int(input("Enter a number : "))
fact=1
if num<0:
    print("FACTORIAL IS NOT APPLICABLE FOR NEGATIVE NUMBER " ,num)
else:
    for i in range(1,num+1):
        fact*=i
    print("FACTORAIL OF ",num," is : ",fact)
        
