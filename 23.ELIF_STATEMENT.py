#ELIF STATEMENT
'''
write a program to library management , in which to calculate the fine for late days :
LATE DAYS            PER DAY FINE
      0                           no fine
   1 - 10                       Rs.100
   11 - 20                     Rs.200
   21 - 30                     Rs.300
above 30                    membership cancelled
'''
late_days=int(input("Enter the late days of returning book : "))
if late_days==0:
    print("GOOD!,no fine")
elif late_days>=1 and late_days<=10:
    print("YOUR FINE AMMOUNT : Rs.",late_days*100)
elif late_days>=11 and late_days<=20:
    print("YOUR FINE AMMOUNT : Rs.",late_days*200)
elif late_days>=21 and late_days<=30:
    print("YOUR FINE AMMOUNT : Rs.",late_days*300)
else:
    print("SORRY,YOUR MEMBERSHIP IS CANCELLED")
    
