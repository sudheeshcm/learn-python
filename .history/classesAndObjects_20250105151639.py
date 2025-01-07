class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Sudheesh', 34)
print(p1)
print(p1.name)
print(type(p1))
print(p1.age)
del p1.age
print(p1.age)

