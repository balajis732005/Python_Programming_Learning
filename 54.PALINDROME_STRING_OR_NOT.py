# To check whether the given string is palindrome or not
s=input("Enter a string : ")
rev_s=""
index=-1
#for index in range(-1,(-(len(s)))-1,-1):
while index>=-len(s):
    rev_s+=s[index]
    index-=1
print("REVERSED STRING : ",rev_s)
if rev_s==s:
    print('"',s,'"'," is an PALINDROME STRING")
else:
    print('"',s,'"'," is not an PALINDROME STRING")
    
