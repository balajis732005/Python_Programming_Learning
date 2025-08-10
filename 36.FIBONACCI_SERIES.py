# FIBONACCI SERIES
n=int(input("Enter the limit : "))
a=0
b=1
add=1
print("FIBONACCI SERIES upto ",n,"terms : ")
print(a,end="  ")
print(b,end="  ")
for i in range(0,n-2):
    c=a+b
    print(c,end="  ")
    add+=c
    a=b
    b=c
print("\nSUM OF FIBONACCI SERIES upto ",n," terms : ",add)
    

