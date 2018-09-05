class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


kitty = Student("Kitty", 85)
Sammy = Student("Sammy", 70)

print("Name: ", kitty.name, " Grade: ", kitty.grade)
print("Name: ", Sammy.name, " Grade: ", Sammy.grade)
print("")

class Bottle:
    element = "sugar"
    def __init__(self, drink, color, type):  #Constructor

        self.drink = drink
        self.color = color
        self.type = type


derp = Bottle("Coke", "Black", "large") #instance variable
otherderp = Bottle("Fanta", "Orange", "Medium")

print("Drink: ", derp.drink, " Color: ", derp.color, " Size: ", derp.type)
print("Drink: ", otherderp.drink, " Color: ", otherderp.color, " Size: ", otherderp.type)
print("")

print("Major Element: ", Bottle.element) #Class variable


class Fighter:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10


    def attack(self, otherguy): #requires one argument
        #method --functions inside of a class are not called
        # functions they're methods!
        otherguy.health = otherguy.health - self.damage
        print("{} attacks {}!".format(self.name, otherguy.name))
        print("{} loses {} health points!".format(otherguy.name, otherguy.damage))

    def __str__(self): #Dunder method
        return "{}: {}".format(self.name, self.health)
        #the first bracket pair has name, second bracket pair has health

rocky = Fighter("Rocky")
me = Fighter("Ahmed")

#print(rocky.name)
#print(me.name)
#print("Rocky's health = ", rocky.health)
#print("Ahmed attacked")
me.attack(rocky)
#print("Rocky's health = ", rocky.health)
#print("")
print(rocky) #<__main__.Fighter object at 0x029C2B50>

class Boxer(Fighter):
    def heal(self):
        self.health += 10

eddy = Boxer("Eddy")
eddy.heal()
print(eddy)




