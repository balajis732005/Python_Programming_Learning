# To find which word is startswith the specific letter
#THE PROGRAM MUST PRINT ALL THE WORDS STARTING WITH LETTER 't'
s=input("Enter the sentence : ")
print("INPUT : ",s)
wors=s.split()
print("OUTPUT : ",end=" ")
for i in wors:
    if i.startswith("t"):
        print(i,end=" ")
