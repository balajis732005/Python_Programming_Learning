s=input()
vow=['a','e','i','o','u']
for i in range(0,len(s)-1):
    if s[i].isalpha():
        c=0
        for j in range(i+1,len(s)):
            if s[j] in vow:
                c+=1
        if c%2!=0:
            print(s[i],end="")
