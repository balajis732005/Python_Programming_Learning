# STRINGS ARE IMMUTABLE , WE CANT,N MODIFY IT (APPEND,REPEATING)
s1="WELCOME "
s2="TO PYTHON "
s1+=s2
print("APPEND : ",s1)
print("REPEATING : ",s2*3)
del s2 #We can only delete the string
s1[0]='A'
