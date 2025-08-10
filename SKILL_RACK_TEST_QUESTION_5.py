'''
A number of integers is input as N and number of pairs is input as X,then the program execute by the inputs given , the program must print 1 if the sum of
integers between pairs is 0 otherwise print 0.
INPUT1:
7 3
1 -1 -1 1 1 1 1
1 4
3 6
1 7
OUTPUT1:
1 0 0
EXPLANATION1:
In first line of input => 7 denotes no.of integers(1,-1,-1,1,1,1,1) and 3 denotes no.of pairs((1,4),(3,6),(1,7))
pair 1(1 to 4)=>1-1-1+1=>0 so print-1
pair 2(3 to 6)=>-1+1+1+1=>2 so print-0
pair 3(1 to 7)=>1-1-1+1+1+1+1=>3 so print-0
'''
N,X=input("Enter the no.of integers and pairs should be split by space : ").split()
N=int(N)
X=int(X)
val=list(map(int,input("Enter the integers : ").split()))
pair=[]
for i in range(0,X):
    a,b=input("Enter pair should be split by space : ").split()
    pair.append(int(a))
    pair.append(int(b))
add=0
print("OUTPUT : ",end="")
for i in range(0,len(pair),2):
    for j in range(pair[i]-1,pair[i+1]):
        add+=val[j]
    if add==0:
        add=0
        print(1,end=" ")
    else:
        add=0
        print(0,end=" ")
    
