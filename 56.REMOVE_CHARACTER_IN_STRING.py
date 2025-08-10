#To remove all the occurences of given character in a string
s=input("Enter a string : ")
ch=input("Enter the character to be removed : ")
new=""
for i in s:
    if i!=ch:
        new+=i
print("OUTPUT : ",new)

    
