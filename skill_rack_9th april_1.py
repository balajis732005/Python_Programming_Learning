s=input()
t=input()
s=list(s)
t=list(t)
for i in range(0,len(s)):
    if s[i] in t:
        s[i]=chr(ord(s[i])-32)
print(s)
