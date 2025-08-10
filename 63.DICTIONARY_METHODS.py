# DICTIONARy AND METHODS
user={"NAME":"BALAJI S","BRANCH":"ECE","AGE":17,"ISGRADUATE":False}
print(type(user))
print(user)
print(user["NAME"])
print(user.get("BRANCH"))
print("KEYS : ",user.keys())
print("VALUES : ",user.values())
print("ITEMS : ",user.items())
for i in user:
    print(i," : ",user[i],end=" / ")
print()
for i in user.values():
    print(i,end="  ")
print()
for i in user.keys():
    print(i,end="  ")
print()
for i,j in user.items():
    print(i,j,end="  ")
print()
user.update({"GENDER":"M"})
print("UPDATE : ",user)
user["AGE"]=18
print("MODIFY : ",user)
user.pop("GENDER")
print("POP : ",user)
user.clear()
print("CLEAR : ",user)
# NESTED DICTIONARY
users={"USER1":{"NAME":"BALAJI S","BRANCH":"ECE","AGE":17,"ISGRADUATE":False},
             "USER2":{"NAME":"RAM","BRANCH":"EEE","AGE":19,"ISGRADUATE":False}}
print("NESTED DICTIONARY : ",users)
print(users["USER2"])
x={"KEY1","KEY2","KEY3"}
y=0
print(dict.fromkeys(x,y))


