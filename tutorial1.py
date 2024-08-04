# classes and objects
""" class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"name={self.name}, age={self.age}, height={self.height}"

person = Person("Mike", 30, 180) """
# print(person)

# if we want to delete whole Person object then just define del function
class Person:
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    def __del__(self):
        Person.amount -= 1

    """ def __del__(self):
        print("Person object deleted") """

person = Person("Mike", 30, 180)

person2 = Person("Sarah", 28, 175)

# del person2
print(Person.amount)