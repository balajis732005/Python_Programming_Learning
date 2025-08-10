#FIBONACCI SERIES USING RECURSION FUNCTION
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter the limit : "))
add=0
print("FIBONACCI SERIES upto ",n," terms : ")
for i in range(0,n):
    print(fibo(i),end=" ")
    add+=fibo(i)
print("\nSUM OF FIBONACCI SERIES upto ",n," terms : ",add)
    
