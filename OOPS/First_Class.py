class First:
    #Constructor
    def __init__(self, name, number, priVar):
        self.name = name
        self.number = number
        self.__priVar = priVar # PRIVATE VARIABLE
        print("First Constructor")

    #Getter
    def getPriVar(self):
        return self.__priVar

    #Setter
    def setPriVar(self, value):
        self.__priVar = value
        return "Setter Done"
#Main
obj = First("Balaji",202,100)
print(obj)
print(obj.name,obj.number)
#print(obj.__priVar) -> Can't Access Private variable
print(obj._First__priVar) # But We can Access the Private Variable Like this
obj.setPriVar("PriVar")
print(obj.getPriVar())