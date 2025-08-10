# To find count of occurence of character in a string
s=input("Enter a string : ")
c=input("Enter which character you want to count : ")
cn=0
list_s=list(s)
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
for i in s1:
    print("'",i,"'","OCCURS ",s.count(i),"TIMES IN A STRING")
for i in s:
    if i==c:
        cn+=1
print("THE CHARACTER ","'",c,"'","IS OCCUR ",cn,"TIMES IN A STRING")
