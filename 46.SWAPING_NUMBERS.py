# SWAP two numbers without using third variable
a,b=map(int,input("Enter 2 numbers : ").split())
print("BY DOING WITH ADDITION AND SUBTRACTION : ")
print("\tBEFORE SWAPING TWO NUMBERS : ")
print("\t\tA : ",a,"\n\t\tB : ",b)
print("\tAFTER SWAPING TWO NUMBERS : ")
a=a+b
b=a-b
a=a-b
print("\t\tA : ",a,"\n\t\tB : ",b)
print("BY DOING WITH MULTIPLICATION AND FLOOR DIVITION : ")
print("\tBEFORE SWAPING TWO NUMBERS : ")
print("\t\tA : ",a,"\n\t\tB : ",b)
print("\tAFTER SWAPING TWO NUMBERS : ")
a=a*b
b=a//b
a=a//b
print("\t\tA : ",a,"\n\t\tB : ",b)

