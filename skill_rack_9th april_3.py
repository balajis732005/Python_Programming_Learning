s=input()
t=input()
t=list(t)
s=list(s)
for i in t:
    if i not in s:
        t.remove(i)
re=[]
i=0
while i<len(s)-1:
    a=s.index(t[i])
    b=1
    for j in range(i+1,len(s)):
        if s[a+b]==t[j]:
            b+=1
        else:
            c=j
            break
    if b>1:
        re.append(s[a:b])
        i=c
    else:
        i+=1
print(re)
    
    
