#CLASS ATTRIBUTES
class student():
    name="BALAJI S"
    age=19
#getattr method
print("BY GETATTR MENTHOD : \n")
print("NAME : ",getattr(student,'name'))
print("AGE : ",getattr(student,'age'))
print("GENDER : ",getattr(student,'gender','No such attribute'))
#Dot Notation
print("\nBY DOT NATION METHOD : \n")
print("NAME : ",student.name)
print("AGE : ",student.age)
#setattr method
print("\nBY SETATTR METHOD : \n")
setattr(student,'name',"NEW BALAJI S")
print("NAME : ",student.name)
setattr(student,'gender',"MALE")
print("GENDER : ",student.gender)
#SET BY  DOT METHOD
print("\nBY DOT NATION METHOD : \n")
student.city="CHENNAI"
print("CITY : ",student.city)
#DELETION
#delattr method
print("\nBY DELATTR METHOD : \n")
print("BEFORE DELETION : ",student.__dict__)
delattr(student,'city')
print("AFTER DELETION : ",student.__dict__)
#Dot Del method
print("\nBY DOT NOTION DEL METHOD : \n")
print("BEFORE DELETION : ",student.__dict__)
del student.gender
print("AFTER DELETION : ",student.__dict__)
