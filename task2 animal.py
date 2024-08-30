class Animal:
    def __init__(self, name):
        self.name = name
 
    def make_sound(self):
        pass
 
 
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow"
 
c = Cat("Bella")  
print(c.make_sound()) 