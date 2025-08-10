#COUNT ODD INTEGERS IN A WORD
lis=list(map(int,input("Enter the list : ").split()))
alp=["One","Two","Three","Four","Five"]
c=0
for i in lis:
    if i%2!=0:
        c+=1
if c!=0:
    print(alp[c-1])
else:
    print("Zero")
