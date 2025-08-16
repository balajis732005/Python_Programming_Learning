class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I {self.age} olds")
    
class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    
    def speak(self):
        print("Bark")
    
class Cat(Pet):
    def speak(self):
        print("Meow")
    
p = Pet("Pet",20)
p.show()
d = Dog("Dog",25,"Brown")
d.show()
d.speak()
c = Cat("Cat",30)
c.show()
c.speak()
    