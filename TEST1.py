#2D MATRIX INPUT AND PRINT
r=int(input("ROW : "))
c=int(input("COLOUMN : "))
lis=[]
for i in range(0,r):
    lis+=list(map(int,input("Enter : ").split()))
print(lis)
print("MATRIX : ")
a=0
for i in range(0,r):
    for j in range(0,c):
        print(lis[a],end=" ")
        a+=1
    print()
print("TRANSPOSE OF MATRIX : ")
for i in range(0,r):
    print(lis[i],end=" ")
    print(lis[i+r],end=" ")
    print(lis[i+2*r],end=" ")
    print()
