#PRINTING LIST ELEMENTS WITHOUT BRACKET
list1=["BALA","KALA","MAN"]
list2=[1,2,3,4,5]
#METHOD - 1[Using for loop]
for i in list1:
    print(i,end=" ")
print()
for j in list2:
    print(j,end=" ")
print()
#METHOD - 2[Using join() function]
print(" ".join(list1))
print(" ".join(map(str,list2)))
#METHOD - 3[Using *operator]
print(*list1,sep=" ")
print(*list2,sep=" ")
