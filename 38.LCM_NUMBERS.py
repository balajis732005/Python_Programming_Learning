# To find the LCM(Least Common multiple) of numbers
num=int(input("Enter you want to find LCM for 2 numbers or 3 numbers(2 or 3) : "))
if num==2:
    n1,n2=map(int,input("Enter 2 numbers : ").split())
    if n1>n2:
        maxi=n1
    else:
        maxi=n2
    for i in range(maxi,(n1*n2)+1):
        if i%n1==0 and i%n2==0:
            lcm=i
            break
    print("LCM of numbers ",n1,n2," is : ",lcm)
elif num==3:
    n1,n2,n3=map(int,input("Enter 3 numbers : ").split())
    if n1>n2 and n1>n3:
        maxi=n1
    elif n2>n3:
        maxi=n2
    else:
        maxi=n3
    for i in range(maxi,(n1*n2*n3)+1):
        if i%n1==0 and i%n2==0 and i%n3==0:
            lcm=i
            break
    print("LCM of numbers ",n1,n2,n3," is : ",lcm)
