class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, major, gpa):
        super().__init__(name, age, gender)
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, Major: {self.major}, GPA: {self.gpa}"

s=Student("shemeema",24,"female","python","4.0")
print(s)