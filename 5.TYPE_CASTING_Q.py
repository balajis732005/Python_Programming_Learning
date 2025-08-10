'''Print the following message by gettint "Anand",15,2021 as input=>
   Dear #Anand#,
   You have #15# days of leave balance for this
   Year(#2021#). '''
#SOLUTION :
name,day,year=input("Enter your name : "),int(input("Enter a day : ")),int(input("Enter a year : "))
print("Dear "+name+",")
print("You have "+str(day)+" days of leave balance for this")
print("Year("+str(year)+").")
