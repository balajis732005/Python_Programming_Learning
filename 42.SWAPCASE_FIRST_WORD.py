# To swapcase the first word of the sentence
s=input("Enter the sentence : ")
#METHOD 1
print("\nMETHOD 1 : \n")
print("INPUT : ",s)
first=" "
for i in s:
    if i==" ":
        break
    else:
        first+=i.strip()
first_s=first.swapcase()
length_first=len(first)
second=" "
for i in range(0,len(s)):
    if i<length_first:
        continue
    else:
        second+=s[i]
print("OUTPUT : ",first_s+second)
#METHOD 2
print("\nMETHOD 2 : \n")
print("INPUT : ",s)
words=s.split()
print("OUTPUT : ",end=" ")
print(words[0].swapcase(),end=" ")
for i in words[1::]:
    print(i,end=" ")
