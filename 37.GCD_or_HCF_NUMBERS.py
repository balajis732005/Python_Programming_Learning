# To find the GCD(Greatest Common divisor) or HCF(Highest Common Factor) of numbers
num=int(input("Enter you want to find GCD for 2 numbers or 3 numbers(2 or 3) : "))
if num==2:
    n1,n2=map(int,input("Enter 2 numbers : ").split())
    if n1<n2:
        mini=n1
    else:
        mini=n2
    for i in range(1,mini+1):
        if n1%i==0 and n2%i==0:
            gcd=i
    print("GCD of numbers ",n1,n2," is : ",gcd)
elif num==3:
    n1,n2,n3=map(int,input("Enter 3 numbers : ").split())
    if n1<n2 and n1<n3:
        mini=n1
    elif n2<n3:
        mini=n2
    else:
        mini=n3
    for i in range(1,mini+1):
        if n1%i==0 and n2%i==0 and n3%i==0:
            gcd=i
    print("GCD of numbers ",n1,n2,n3," is : ",gcd)
