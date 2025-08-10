#SUM NUMBERS UPTO N
n=int(input("Enter the limit : "))
sum_n=0
sum_e=0
sum_o=0
for i in range(0,n+1):
    sum_n+=i
    if i%2==0:
        sum_e+=i
    else:
        sum_o+=i
print("SUM OF NUMBERS UPTO ",n," is : ",sum_n)
print("SUM OF EVEN NUMBERS UPTO ",n," is : ",sum_e)
print("SUM OF ODD NUMBERS UPTO ",n," is : ",sum_o)
