lst=list(map(int,input("Enter the values of list : ").split()))
for i in range(1,len(lst)):
    for j in range(i,0,-1):
        if lst[j-1]>lst[j]:
            temp=lst[j]
            lst[j]=lst[j-1]
            lst[j-1]=temp
print("OUTPUT : ",lst)
