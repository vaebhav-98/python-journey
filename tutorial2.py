# Inheritance
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name : {}, Age : {}, Height : {}".format(
            self.name, self.age, self.height
        )

    def get_older(self, years):
        self.age += years


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary
    
    def __str__(self):
        return super(Worker, self).__str__() + f" Salary {self.salary}"

    def calc_yearly_salary(self):
        return self.salary * 12

worker1 = Worker("Henry", 40, 176, 300)
""" print(worker1)
print(worker1.calc_yearly_salary()) """


# Operator Overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

vector1 = Vector(2, 5)
vector2 = Vector(6, 3)

print(vector1)
print(vector2)

print(vector1 - vector2)