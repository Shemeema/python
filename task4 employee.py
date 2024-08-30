class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, job_title, salary, num_employees_managed):
        super().__init__(name, job_title, salary)
        self.num_employees_managed = num_employees_managed

    def __str__(self):
        return f"Name: {self.name}, Job Title: {self.job_title}, Employees Managed: {self.num_employees_managed}"


m = Manager("John", "Project Manager", 70000, 10)
print(m)
