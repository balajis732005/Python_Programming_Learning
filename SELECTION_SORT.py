lst=list(map(int,input("Enter the list of values : ").split()))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("OUTPUT : ",lst)
