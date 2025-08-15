#TYPE CASTING==>changing the data type but it is temparary
#data types - int,str,float
otp=123456 #int
print("otp is "+str(otp)) #type casting to string
print("Data type of otp after type casting : ",type(otp))
num=12.5 #float
print(int(num)+1) #type casting to integer
print(str(num)+str(1)) #type casting to string
print("Data type of num after type casting : ",type(num))
#If we want to change the data type permanently by type casting the;
num=int(num)
print(num)
print(type(num))
