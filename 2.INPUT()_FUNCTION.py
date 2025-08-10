#Input() fuction
#defult return type of the input fuction is "string"
''' Write a program to change the height in centimeter to inches ? '''
name=input("Enter your name : ")
print("NAME : ",name)
lucky_num=input("Enter your lucky number : ")
print("LUCKY NUMBER : ",lucky_num)
print("Data type of lucky_num : ",type(lucky_num))
height=float(input("Enter your height in centimeters and it will automatically stored as float : "))
print("Data type of height : ",type(height)) #float
height_in_inches=height/2.54
print("HEIGHT IN INCHES with floating value : ",height_in_inches)
height=input("Enter your height in centimeters : ")
print("Data type of height : ",type(height)) #string
height_in_inches=height/2.54
print("HEIGHT IN INCHES : ",height_in_inches)


