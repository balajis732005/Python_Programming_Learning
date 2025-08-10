'''
YOU HAVE TO ADD AN INTEGER IN THE CORRECT POSITION IN A SORTED LIST.
'''
#METHOD 1
print("METHOD 1 : ")
lis=list(map(int,input("Enter the sorted list elements : ").split()))
n=int(input("Enter a number to be added : "))
temp=lis
print("INPUT : ",lis)
for i in range(len(lis)-1,-1,-1):
    if n>lis[i]:
        lis.insert(i+1,n)
        break
print("OUTPUT : ",lis)

#METHOD 2
print("METHOD 2 : ")
lis1=list(map(int,input("Enter the sorted list elements : ").split()))
n=int(input("Enter a number to be added : "))
print("INPUT : ",lis1)
lis1.append(n)
lis1.sort()
print("OUTPUT : ",lis1)
