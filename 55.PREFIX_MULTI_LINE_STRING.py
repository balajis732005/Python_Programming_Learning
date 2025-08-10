# To add prefix text to all the lines in a string
'''
EXAMPLE:

INPUT : My name is BALAJI S.I am studying in Chennai institute of technology.I am stduying ECE(1st year).

OUTPUT : *My name is BALAJI S.
                  *I am studying in Chennai institute of technology.
                  *I am stduying ECE(1st year).
'''
s=input("Enter multiline string by using dot : ")
print("INPUT : ",s)
s=s.split(".")
print("OUTPUT : ",end="")
for i in s:
    print("*"+i)
    print("\t",end=" ")



