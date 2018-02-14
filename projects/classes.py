class Animal:
    def __init__(self, name):
        self.name = name

class Dog (Animal):
    def woof (self):
        print("woof")

class Cat (Animal):
    def meow (self):
        print("meow")

print(Cat)