#FINALLY BLOCK
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except:
    print("ERROR")
else:
    print("SUCCES")
finally:
    print("EXECUTED")
