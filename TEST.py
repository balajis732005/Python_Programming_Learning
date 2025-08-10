n=int(input())
lis=list(map(int,input().split()))
new=[]
b=1
for i in range(0,len(lis)):
    a=0
    for j in range(b,len(lis)):
        new.append(sum(lis[a:j+1]))
        a+=1
    b+=1
print(max(new))

















