class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, salary, name, age):
        Person.__init__(self, name, age)
        self.salary = salary
    def display_details(self):
        Person.display_details(self)
        print("Salary:", self.salary)

max = Person("Max", 18)
max.display_details()
etienne = Employee(1200, "Etienne", 10)
etienne.display_details()
