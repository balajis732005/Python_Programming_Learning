'''
The set of characters with equal number of vowels and consonants are paased as input.The program must print the vowels and consonants with replacing
the input .
INPUT1:
aexyiojd
OUTPUT1:
xyaeidio
INPUT2:
rdiopdae
OUTPUT2:
iordaepd
'''
s=input("Enter the input : ")
vowels='aeiouAEIOU'
v=[]
c=[]
for i in s:
    if i in vowels:
        v.append(i)
    else:
        c.append(i)
a=0
b=0
print("OUTPUT : ",end="")
for i in s:
    if i in vowels:
        for i in range(a,len(c)):
            print(c[i],end="")
            a+=1
            break
    else:
        for i in range(b,len(v)):
            print(v[i],end="")
            b+=1
            break
