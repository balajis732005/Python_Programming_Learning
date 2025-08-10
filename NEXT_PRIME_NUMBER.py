'''
A number N is input through the keyboard.The must print the next prime number of N.
INPUT1:
13
OUTPUT1:
17
INPUT2:
1
OUTPUT3:
2
'''
N=int(input("Enter the number to start : "))
f=0
for i in range(N+1,(N*1000000)+1):
    for j in range(1,i+1):
        if i%j==0:
            f+=1
    if f==2:
        print("NEXT PRIME NUMBER : ",i)
        break
    else:
        f=0
    
        
