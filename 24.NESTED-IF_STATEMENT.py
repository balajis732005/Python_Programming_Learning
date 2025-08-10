#NESTED IF STATEMENT
'''
MARKING SYSTEM IN SCHOOLS
GRADE       AVERAGE
    A             above 90
    B              81-89
    C              71-80
    D              61-70
NO GRADE
BUT PASS      other
    minimum pass mark is 35
    '''
m1,m2,m3,m4,m5,m6=map(int,input("Enter 6 subjects marks : ").split())
# if you want to get input integer values by using split function use this method
total=m1+m2+m3+m4+m5+m6
average=total//6
percentage=total/6.0
print("TOTAL : ",total,"/600")
print("AVERAGE : ",average)
print("PERCENTAGE : ",percentage,"%")
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35 and m6>=35:
    print("RESULT : PASS")
    if average>=90:
        print("GRADE A.")
    elif average<=89 and average>=81:
        print("GRADE B.")
    elif average<=80 and average>=71:
        print("GRADE C.")
    elif average<=70 and average>=61:
        print("GRADE D.")
    else:
        print("NO GRADE BUT PASS.")
else:
    print("RESULT : FAIL")
    
