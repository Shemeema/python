class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id=employee_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Employee Id: {self.employee_id}"

e=employee("shemeema",24,"py003")
print(e)