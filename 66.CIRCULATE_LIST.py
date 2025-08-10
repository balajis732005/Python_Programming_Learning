#circulate list upto n terms
#START
lis=list(map(int,input("Enter the list of elelments split by space : ").split()))
n=int(input("Enter how many times to circulate : "))
for i in range(1,n+1):
    for j in range(-1,-(len(lis)),-1):
        lis[j],lis[j-1]=lis[j-1],lis[j]
    print(i,"th","ROTATION",lis)
#END
