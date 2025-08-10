# To check whether the given year is leap year or not
year=int(input("Enter a year : "))
print("YEAR : ",year)
if year%100==0:
    if year%400==0:
        print("YEAR ",year," is an LEAP YEAR")
    else:
        print("YEAR ",year," is not an LEAP YEAR")
else:
    if year%4==0:
        print("YEAR ",year," is an LEAP YEAR")
    else:
        print("YEAR ",year," is not an LEAP YEAR")
        
        
