# TABLES UPTO N TERMS
num=int(input("Enter the number : "))
n=int(input("Enter the limit (IF DIVISION/FLOOR DIVISION/MODULUS =>give n-1): "))
table=input("Enter which table you want\nADDITION - '+'\nSUBTRACTION - '-'\nMULTIPLICATION - 'X'\nDIVISION - '/'\nMODULAS - '%'\nEXPONENT(or)POWER - '**'\nFLOOR DIVISION - '//'\nYOUR CHOICE : ")
for i in range(0,n+1):
    if table=='+':
        print(num,table,i,"=",num+i)
    elif table=='-':
        print(num,table,i,"=",num-i)
    elif table=='X':
        print(num,table,i,"=",num*i)
    elif table=='/':
        print(num,table,i+1,"=",num/(i+1))
    elif table=='%':
        print(num,table,i+1,"=",num%(i+1))
    elif table=='**':
        print(num,table,i,"=",num**i)
    elif table=='//':
        print(num,table,i+1,"=",num//(i+1))
        
