'''
Two numbers N and X are paased as input.The program must print the multiple of N(starting from 1)and must stop when the multiple is divisible by X.
INPUT1:
5
8
OUTPUT!:
5 10 15 20 25 30 40
INPUT2:
8
4
OUTPUT2:
8
INPUT3:
6
7
OUTPUT3:
6 12 18 24 30 36 42
'''
N=int(input("Enter the number : "))
X=int(input("Enter the number to be X : "))
for i in range(N,(N*X)+1,N):
    if i%X==0:
        print(i,end=" ")
        break
    else:
        print(i,end=" ")
