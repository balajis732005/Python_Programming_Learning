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
print("LARGEST NUMBER : ",maxi)
print("SMALLEST NUMBER : ",mini)
