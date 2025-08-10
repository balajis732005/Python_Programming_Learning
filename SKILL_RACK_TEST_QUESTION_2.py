'''
The input contain 3 integers are split by space.The must print the multiples of middle value from other numbers
INPUT1:
55 5 10
OUTPUT1:
10 20 30 40 50
INPUT2:
35 45 10
OUTPUT2:
35
'''
num=list(map(int,input("Enter the input : ").split()))
mini=min(num)
maxi=max(num)
num.remove(mini)
mid=min(num)
print("OUTPUT : ",end="")
for i in range(mini,maxi+1):
    if i%mid==0:
        print(i,end=" ")
