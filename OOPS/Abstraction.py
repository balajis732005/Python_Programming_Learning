from abc import ABC, abstractmethod

class ABS(ABC):

    def get_dataBase(self):
        print("Connected with DataBase")

    @abstractmethod
    def security(self):
        print("Security layer Cleared")

class Child(ABS):

    def security(self):
        print("Child Class Cleared the Security")

    def childImp(self):
        print("Child Implementation")

c = Child()

if __name__ == '__main__':
    c.childImp()
    c.get_dataBase()