class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return("Woof")

class Cat(Animal):
    def talk(self):
        return("Meow")

kitten = Cat("Panther")
print(kitten.talk())

doggy = Dog("Yoda")
print(doggy.talk())

goat = Animal("Benny")
print(goat.talk())
