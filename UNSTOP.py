def myfun(s):
    s=list(s)
    s=sorted(s)
    word=["one","two","three","four","five",
    "six","seven","eight","nine"]
    first_sin=['z','o','e','n']
    first_dou=['t','f','s']
    re=[]
    i=0
    while s!="":
        if i==len(s)-1:
            i=0
        if s[i] in first_sin:
            a=first_sin.index(s[i])
            if a==0 and 'e' in s and 'r' in s and 'o' in s:
                s.remove(s[i])
                s.remove('e')
                s.remove('r')
                s.remove('o')
                re.append(0) 
            elif a==1 and 'n' in s and 'e' in s:
                s.remove(s[i])
                s.remove('n')
                s.remove('e')
                re.append(1)
            elif a==2 and 'i' in s and 'g' in s and 'h' in s and 't' in s:
                s.remove(s[i])
                s.remove('i')
                s.remove('g')
                s.remove('h')
                s.remove('t')
                re.append(8)
            elif a==3 and 'i' in s and 'e' in s:
                s.remove(s[i])
                s.remove('i')
                s.remove('n')
                s.remove('e')
                re.append(9)
        elif s[i] in first_dou:
            a=first_dou.index(s[i])
            if a==0:
                if 'w' in s:
                    s.remove(s[i])
                    s.remove('w')
                    s.remove('o')
                    re.append(2)
                else:
                    s.remove(s[i])
                    s.remove('h')
                    s.remove('r')
                    s.remove('e')
                    s.remove('e')
                    re.append(3)
            elif a==1:
                if 'u' in s:
                    s.remove(s[i])
                    s.remove('o')
                    s.remove('u')
                    s.remove('r')
                    re.append(4)
                else:
                    s.remove(s[i])
                    s.remove('i')
                    s.remove('v')
                    s.remove('e')
                    re.append(5)
            elif a==2:
                if 'i' in s:
                    s.remove(s[i])
                    s.remove('i')
                    s.remove('x')
                    re.append(6)
                else:
                    s.remove(s[i])
                    s.remove('e')
                    s.remove('v')
                    s.remove('e')
                    s.remove('n')
                    re.append(7)
    return re
n=int(input())
lis=[]
for i in range(0,n):
    lis.append(input())
for i in range(0,n):
    new=myfun(lis[i])
    new=sorted(new)
    if sum(new)==0:
        print(0)
    elif 0 in new:
        new[0],new[1]=new[1],new[0]
        for j in new:
            print(j,end="")
    else:
        for j in new:
            print(j,end="")
