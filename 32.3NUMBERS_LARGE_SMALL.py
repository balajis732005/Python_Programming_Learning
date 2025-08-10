# To find the largest and smallest among 3 numbers
n1,n2,n3=map(int,input("Enter 3 numbers : ").split())
print("LARGEST NUMBERS : \n")
if n1>n2 and n1>n3:
    print(n1,"is FIRST LARGEST")
    if n2>n3:
        print(n2,"is SECOND LARGEST")
    else:
        print(n3,"is SECOND LARGEST")
elif n2>n3:
    print(n2,"is FIRST LARGEST")
    if n1>n3:
        print(n1,"is SECOND LARGEST")
    else:
        print(n3,"is SECOND LARGEST")
else:
    print(n3,"is FIRST LARGEST")
    if n1>n2:
        print(n1,"is SECOND LARGEST")
    else:
        print(n2,"is SECOND LARGEST")
print("\nSMALLEST NUMBERS : \n")
if n1<n2 and n1<n3:
    print(n1,"is FIRST SMALLEST")
    if n2<n3:
        print(n2,"is SECOND SMALLEST")
    else:
        print(n3,"is SECOND SMALLEST")
elif n2<n3:
    print(n2,"is FIRST SMALLEST")
    if n1<n3:
        print(n1,"is SECOND SMALLEST")
    else:
        print(n3,"is SECOND SMALLEST")
else:
    print(n3,"is FIRST SMALLEST")
    if n1<n2:
        print(n1,"is SECOND SMALLEST")
    else:
        print(n2,"is SECOND SMALLEST")
    
