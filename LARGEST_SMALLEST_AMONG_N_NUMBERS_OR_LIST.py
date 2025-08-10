# TO FIND LARGEST AND SMALLEST AMONG N NUMBERS
N=int(input("Enter how many numbers : "))
list1=[]
for i in range(1,N+1):
    ni=int(input("Enter a number : "))
    list1.append(ni)
maxi=list1[0]
for i in list1:
    if i>maxi:
        maxi=i
mini=list1[0]
for i in list1:
    if i<mini:
        mini=i
print("FIRST LARGEST NUMBER : ",maxi)
print("FIRST SMALLEST NUMBER : ",mini)
list1.remove(maxi)
list1.remove(mini)
maxi2=list1[0]
for j in list1:
    if j>maxi2:
        maxi2=j
mini2=list1[0]
for j in list1:
    if j<mini2:
        mini2=j
print("SECOND LARGEST NUMBER : ",maxi2)
print("SECOND SMALLEST NUMBER : ",mini2)


