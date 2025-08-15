class StaticLearn:

    #Static Variable
    __cusId = 0

    def __init__(self):
        self.cusId = StaticLearn.__cusId
        StaticLearn.__cusId += 1

    def getCusId_Self(self):
        return self.__cusId
    
    @staticmethod
    def getCusId():
        return StaticLearn.__cusId

#Main
s1 = StaticLearn()
print(s1.getCusId()," - ",s1.getCusId_Self())
print(s1.cusId)
s2 = StaticLearn()
print(s2.getCusId()," - ",s2.getCusId_Self())
print(s2.cusId)