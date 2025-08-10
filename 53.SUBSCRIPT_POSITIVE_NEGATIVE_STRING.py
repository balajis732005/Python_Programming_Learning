# To the characters of string along positive subscript
s=input("Enter a string : ")
print("\nPOSITIVE SUBSCRIPT : \n")
index=0
for i in s:
#while index<=len(s):
    print("SUBSCRIPT [",index,"] : ",i)
    #print("SUBSCRIPT [",index,"] : ",s[index])
    index+=1
print("\nNEGATIVE SUBSCRIPT : \n")
index=-1
#while index>=-(len(s)):
for index in range(-1,(-(len(s)))-1,-1):
    #print("SUBSCRIPT [",index,"] : ",s[index])
    print("SUBSCRIPT [",index,"] : ",s[index])
    index-=1

