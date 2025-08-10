# LIST COMPREHENSION
# SYNTAX => list=[expression for variable in  range]
even=list(range(0,11,2))
print("EVEN NUMBERS : ",even)
odd=list(range(1,11,2))
print("ODD NUMBERS : ",odd)
l=int(input("Enter the limit : "))
squares=[x**2 for x in range(0,l+1)]
print("SQUARES : ",squares)
