'''
A strings S is input from user and character ch is also input from user.Then the program check how many words are end with ch and print that words.
if all words are no endwith ch means then print -1.

INPUT1:
goodmorning goodevening not bad
g
OUTPUT1:
goodmorning goodevening
INPUT2:
welcome to python
x
OUTPUT2:
-1

'''
S=input("Enter the words : ").split()
ch=input("Enter the character : ")
c=0
print("OUTPUT : ")
for i in S:
    if i.endswith(ch):
        print(i,end=" ")
    else:
        c+=1
if c==len(S):
    print(-1)
