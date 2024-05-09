class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Mike', 30)
print(p.name)
print(p.age)

choice = input("Which attribute do you want to change: ")
value = input("What do you want to change this to: ")

setattr(p, choice, value)

print(hasattr(p, "name"))
delattr(p, "name")

print(p.name)
print(p.age)
print(p.height)
