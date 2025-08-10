#ASCII DECRYPTION
s=input("Enter a string : ")
i=0
while i<len(s):
    if s[i].isdigit():
        a=s[i]
        while int(a)<97:
            i+=1
            a+=s[i]
        print(chr(int(a)),end="")
        i+=1
    else:
        print(s[i],end="")
        i+=1
            
            
