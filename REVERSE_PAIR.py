n=int(input())
lis=list(map(int,input().split()))
c=0
temp=[*lis]
for i in range(0,n):
    for j in range(i+1,n):
        if lis[i] in temp and lis[j] in temp:
            if lis[i]==int(str(lis[j])[::-1]) or lis[j]==int(str(lis[i])[::-1]):
                c+=1
                lis[i]=-1
                lis[j]=-1
                break
print(c)
