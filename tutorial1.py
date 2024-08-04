# classes and objects
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"name={self.name}, age={self.age}, height={self.height}"

person = Person("Mike", 30, 180)
print(person)