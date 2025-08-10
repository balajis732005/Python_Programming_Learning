s=input()
s=list(s)
print(s)
lis=[]
temp=[]
for i in s:
    if i not in temp:
        lis.append(i)
        temp.append(i)
print(lis)
c=0
c1=0
for i in lis:
    for j in s:
        if i==j:
            print(j)
            s.remove(j)
            c+=1
        else:
            break
    print(s)
    if c>=2:
        c1+=1
    c=0
if c1==len(lis):
    print("YES")
else:
    print("NO")
    
