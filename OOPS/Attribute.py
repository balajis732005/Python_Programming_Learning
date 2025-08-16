class Top:

    no_of_obj = 0
    classVar = 0

    def __init__(self, name):
        self.name = name
    
    def set_no_of_obj(self, num):
        Top.no_of_obj = num
    
    def get_no_of_obj(self):
        return Top.no_of_obj
    
    @classmethod
    def set_class_var(cls):
        cls.classVar += 1
    
    @classmethod
    def get_class_var(cls):
        return cls.classVar

t1 = Top("Top1")
t2 = Top("Top2")
Top.no_of_obj = 5
print(t1.get_no_of_obj())
print(t2.get_no_of_obj())
t1.no_of_obj = 10 # Not Work
print(t1.no_of_obj) # Specific to t1
print(t1.get_no_of_obj()) # general to Top
print(t2.get_no_of_obj()) # general to Top
t1.set_no_of_obj(10)
t2.set_no_of_obj(20)
print(t1.no_of_obj) # Specific to t1
print(t2.no_of_obj) # Specific to t2
print(t1.get_no_of_obj()) # general to Top
print(t2.get_no_of_obj()) # general to Top
t3 = Top("Top3")
t3.set_class_var()
print(t3.get_class_var())