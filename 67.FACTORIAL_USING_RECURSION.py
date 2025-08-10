#FACTORIAL OF A NUMBER USING RECURSION FUNCTION
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number : "))
if n<0:
    print("NEGATIVE VALUES LIKE ",n," IS NOT APPLICABLE FOR FACTORIAL")
else:
    print("FACTORIAL OF NUMBER ",n," is : ",fact(n))
