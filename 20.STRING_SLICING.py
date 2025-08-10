#STRING SLICING
#str[start:end:step] =>end=n-1
#when start=-ve the end=n+1
s="BALAJI's PYTHON PROGRAMMING"
print("STRING : ",s,"\n")
print("1 : ",s[0])
print("2 : ",s[-1])
print("3 : ",s[0:])
print("4 : ",s[-1:]) # end value is must for negative slice
print("5 : ",s[:7])
print("6 : ",s[:-7]) #The default start value is 0
print("7 : ",s[0:10])
print("8 : ",s[-1:-10:-1]) #step value is must when start with negative slice
print("9 : ",s[5:16])
print("10 : ",s[-5:-16:-1]) #step value is must when start with negative slice
                                          #when start value is negative the end=n+1
print("11 : ",s[-1:10:-1]) #step value is must when start with negative slice
                                         #when start value is negative the end=n+1
print("12 : ",s[0:16:2])
print("13 : ",s[-1:-16:-2]) #when start value is negative the end=n+1
print("14 : ",s[:16:2])
print("15 : ",s[:-16:-2]) #when step value is negative the default start=-1
print("16 : ",s[::3])
print("17 : ",s[::-4]) #when step value is negative the default start=-1
print("18 : ",s[0::2])
print("19 : ",s[-1::-3]) #when start value is negative the end=n+1
print("20 : ",s[:11:])
print("21 : ",s[:-11:]) #The default start value is 0
print("22 : ",s[:-11:-1])#when step value is negative the default start=-1
print("23 : ",s[-1:10:-1]) #when start value is negative the end=n+1
print("REVERSE : ",s[::-1]) #when step value is negative the default start=-1
