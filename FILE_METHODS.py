#C:/TEST.txt/
a=input("Enter :")
f1=open(a,"w")
f=open(a,"r")
l=["BALAJI\n","PYTHON\n","CHENNAI\n","ECE\n","MAN\n"]
f1.writelines(l)
for i in range(0,5):
    line=next(f)
    print(line)
print("SUCCES")
f.close()
