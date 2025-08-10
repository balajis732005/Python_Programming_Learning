#STRING METHODS
a="BAlaji S"
print("METHODS : \n")
print("UPPER() : ",a.upper())
print("LOWER() : ",a.lower())
print("CAPITALIZE() : ",a.capitalize())
print("TITLE() : ",a.title())
print("COUNT() : ",a.count("a",0,2))
print("FIND() : ",a.find("a",2,5))
print("REPLACE() [a=>@]: ",a.replace("a","@"))
print("CENTER() : ",a.center(16,"#"))
print("SWAPCASE() : ",a.swapcase())
print("CASEFOLD() : ",a.casefold())
print("ZFILL() [string] : ",a.zfill(16))
b="Balaji\nis\ngood\ncoder"
print("SPLITLINES() : ",b.splitlines())
print("SPLITLINES(TRUE) : ",b.splitlines(True))
c="Hellow,to,the,world"
print("SPLIT() : ",c.split())
print("SPLIT(COMMA) : ",c.split(","))
print("RSPLIT() : ",c.rsplit(",",2))
print("RFIND() [start] : ",c.rfind("the"))
print("RFIND() [end] : ",c.rfind("o"))
print("RINDEX() [start] : ",c.rindex("the"))
print("RINDEX() [end] : ",c.rindex("o"))
d="     BALAJI     "
print("STRIP() : ",len(d.strip()))
print("LSTRIP() : ",len(d.lstrip()))
print("RSTRIP() : ",len(d.rstrip()))
e="07/03/2005"
print("PARTITION() [Date] : ",e.partition("/"))
print("RPARTITION()[Date] : ",e.rpartition("/"))
f="MY NAME IS BALAJI"
print("ENCODE() : ",f.encode())
print("PARTITION() [Word] : ",f.partition("NAME"))
print("RPARTITION()[Word] : ",f.rpartition("IS"))
g="B\tA\tL\tA\tJ\tI"
print("EXPANDTABS() : ",g.expandtabs(20))
h="MY NAME IS {name} , AND MY AGE IS {age} , AND HEIGHT {height:.2f}."
print("FORMAT() : ",h.format(name="BALAJI S",age=17,height=172.3580))
i={"name":"BALAJI S","book":"PYTHON"}
print("FORMAT_MAP() : ","{name}'s last readed Book is {book}.".format_map(i))
j=["APPLE","MANGO","ORANGE"]
print("INDEX() : ",j.index("MANGO"))
print("JOIN() : ","&".join(j))
k="Amma is first god"
print("LJUST() : ",k.ljust(60,"!"))
print("RJUST() : ",k.rjust(60,"!"))
change=k.maketrans("god","GOD")
print("MAKETRANS() and TRANSLATE() : ",k.translate(change))
print("\nBOOLEAN METHODS : \n")
l="BALAJI's HABIT"
print("STARTSWITH() : ",l.startswith("BA"))
print("ENDSWITH() : ",l.endswith("it"))
print("ISUPPER() : ",l.isupper())
print("ISLOWER() : ",l.islower())
print("ISALPHA() : ",l.isalpha())
print("ISASCII() : ",l.isascii())
m="BALAJI007"
print("ISALNUM() : ",m.isalnum())
print("ISNUMERIC() : ",m.isnumeric())
print("ISDIGIT() : ",m.isdigit())
print("ISDECIMAL() : ",m.isdecimal())
print("ISIDENTIFIER() : ",m.isidentifier())
print("ISPRINTABLE() : ",m.isprintable())
print("ISSPACE() : ",m.isspace())
print("ISTITLE() : ",m.istitle())
print("\nASCII FUNCTIONS : \n")
print("ORD() : ",ord("A"))
print("CHR() : ",chr(65))
#ERROR STATEMENT
change=k.maketrans("god","first")
print("MAKETRANS() : ",k.translate(change))




