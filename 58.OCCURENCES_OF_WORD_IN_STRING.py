# Write a program to count the oocurences of each word in a string
s=input("Enter a string : ")
word=input("Enter which word you want to count : ")
wc=0
s=s.split()
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
for i in s1:
    print("'",i,"'","OCCURS",s.count(i),"TIMES IN A STRING")
for i in s:
    if word==i:
        wc+=1
print("THER WORD ","'",word,"'","IS OCCURS ",wc,"TIMES IN A STRING")
        
