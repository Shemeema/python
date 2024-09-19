class Animal:
    def sound(self):
        return "Dog name is jinto"
    
class dog(Animal):
    def sound(self):
        return "Boww...!"


a= Animal()
d=dog()

print(f"{a.sound()} and says {d.sound()}")






class Vehicle:
    def __init__(self,make):
        self.make=make
        
class car(Vehicle):
    def __init__(self,make,model):
        super().__init__(make)
        self.model=model

class electricalcar(car):
    def __init__(self, make,model,year):
        super().__init__(make,model)
        self.year=year


e=electricalcar("Tesla","Model 3",2020)

print(f"make:{e.make},model:{e.model},year:{e.year}")







class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

circle = Circle(5)
square = Square(6)

print("area of circle:",circle.area())  
print("area of square:",square.area())  







class Person:
    def __init__(self, name):
        self.name = name
       

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
       


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
       


class Intern1(Employee):
    def __init__(self, name, employee_id,internship_duration):
        super().__init__(name, employee_id)
        # Student.__init__(self, name, student_id)
        self.internship_duration = internship_duration

class Intern(Student):
    def __init__(self, name, student_id,internship_duration):
        super().__init__(name, student_id)
        self.internship_duration = internship_duration




i = Intern1("shemeema", 1025, "6 months")
I = Intern("shemeema",23,"6 months")
print(f"student name :{i.name}, employee id :{i.employee_id}, student :{I.student_id}, internship Duration :{i.internship_duration}")

