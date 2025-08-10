# To check whether the given number is prime or not
num=int(input("Enter a number : "))
fact=0
for i in range(1,num+1):
    if num%i==0:
        fact+=1
if fact==2:
    print(num," is an PRIME NUMBER")
else:
    print(num," is NOT an PRIME NUMBER")
