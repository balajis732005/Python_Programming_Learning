n=int(input())
lis=list(map(int,input().split()))
new=[]
while sum(lis)!=0:
    s=0
    for i in range(0,len(lis)):
        if lis[i]<0 and len(str(lis[i]))==1:
            s-=abs(lis[i])%10
        elif lis[i]<0:
            s+=abs(lis[i])%10
        else:
            s+=lis[i]%10
        if lis[i]<0:
            lis[i]=-lis[i]
            lis[i]//=10
            lis[i]=-lis[i]
        else:
            lis[i]//=10
    new.append(abs(s))
print(new)
        
