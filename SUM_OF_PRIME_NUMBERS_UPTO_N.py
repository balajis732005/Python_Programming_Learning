#SUM OF PRIME NUMBERS UPTO N TERMS
n=int(input("Enter the limit : "))
c=0
add=0
a=0
print("PRIME NUMBERS upto ",n," terms : ")
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i,",",end=" ")
        add+=i
        a+=1
        c=0
    c=0
print("\nTHERE ARE ",a," PRIME NUMBERS upto ",n," terms")
print("SUM OF PRIME NUMBERS upto ",n," terms : ",add)
