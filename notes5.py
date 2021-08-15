# Object Oriented Programming Python


# Classes and Objects

class Ghanaian():
    ishuman = True 
    enjoys_coding = True 

# create an object 
jesse = Ghanaian() 
# check the type 
print(type(jesse))
print(jesse.ishuman)

# Create a pet class
class Pet():
    isHuman = False 
    owner = "Jesse Mensah"

wonder = Pet() 

# special __init__ method job ?? 
class Pet(): 
    def __init__(self, height):
        self.height = height
    is_animal = True 
    owner = "Jesse Mensah"
cabana = Pet(height=10)
print(cabana.height)

# Create a class circle with radius and color set to anything you want 
class Circle(): 
    def __init__(self, radius, color):
        self.color = color 
        self.radius = radius 
firstcircle = Circle(radius=5, color="brown")

# Keyword arguments & positional arguments ?? 
class AnotherCircle():
    def __init__(self, radius, color="brown"): 
        self.radius = radius 
        self.color = color 
mycircle = AnotherCircle(23)


# Three types of methods usually used in classes,  Instance methods, static methods and class methods 
import math 

class Circle():
    is_Shape = True 

    def __init__(self, radius, color="red"):
        self.radius = radius 
        self.color = color 
    # instance methods always take self as the first positional arguments 
    def area(self):
        return math.pi * self.radius ** 2 

lastcircle = Circle(10) 
print(lastcircle) 

# adding arguments to instance methods 
class Pet():
    def __init__(self, height):
        self.height = height 

    isHuman = False 
    owner = "Jesse Mensah" 
    def is_tall(self, tall_if_at_least):
        return self.height >= tall_if_at_least
chelsea = Pet(10)
print(chelsea.is_tall(20)) 

# str method, used whenever an object is rendered as a string 
class Pet():
    def __init__(self, height, name):
        self.height = height 
        self.name = name 

    is_human = False 
    owner = "Michael Smith"

    def __str__(self):
        return '%s (height: %s cm)' % (self.name, self.height)
my_other_pet = Pet(40, 'Jesse')
print(my_other_pet)

# Static Methods => defined by using @staticmethod decorator. 
# Decorators allow us to alter the behavior of functions and classes. 
# Decorators? more to it but for now think of it as preventing us from using self argument
class Pet(): 
    def __init__(self, height):
        self.height = height 

    is_human = False 
    owner = "Jesse Mensah" 

    @staticmethod 
    def owned_by_mensahfamily():
        return 'Mensah' in Pet.owner 

bubbles = Pet(100) 
bubbles.owned_by_mensahfamily() 

# Class Methods?? , similar to instance methods but 
# instead of instance of object being passed as first positional self argument 
# the class itself is passed as the first argument. 

class African():
    is_Human = True 
    enjoys_sport = True 

    @classmethod 
    def is_sporty_human(cls):
        return cls.is_Human and cls.enjoys_sport
African.is_sporty_human()  
african = African() 
african.is_sporty_human() 

# Properties , used to manage attributes of object 
# ie suppose i have object w height and object property, 
# also want that object to have an area property which is combination of both 

# Understand the need for decorator property 
class Temperature():
    def __init__(self, celsius, fahrenheit): 
        self.celsius = celsius 
        self.fahrenheit = fahrenheit 

freezing = Temperature(0, 32) 
freezing.fahrenheit

# now suppose want to store the temperature in celsius and convert to fah when needed 
class Temperature():
    def __init__(self, celsius): 
        self.celsius = celsius 

    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32 

# can turn fahrenheit into a property, which can be accessed anywhere 
class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius 

    @property 
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32 

freezing = Temperature(100) 
print(freezing.fahrenheit) 


# Setters?? 
# Setters, called when a user assigns a value to a property 
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

    @property 
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name) 

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first 
        self.last_name = last 

customer = Person("Mary", "Lou")
customer.full_name = "Mary Mensah" 
print(customer.last_name) 


# Inheritance, atttributes and methods  from one class to another 
# DRY Principle ?? 
# Does python support mulitple inheritance ?? 
class Pet():
    def __init__(self, name, weight):
        self.name = name 
        self.weight = weight 

class Cat(Pet):
    is_Feline = True 

class Dog(Pet):
    is_Feline = False 
my_cat = Cat('Tebbles', 10)
my_cat.name 

# Overriding methods ?? 


# Multiple Inheritance 
import datetime 
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

class Baby(Person):
    def speak(self):
        print("Blah Blah Blah")

class Adult(Person):
    def speak(self):
        print("Hello, my name is %s" % self.first_name)

class Calender():
    def book_appointment(self, date):
        print('Booking appointment for date %s' % date)

class OrganisedAdult(Adult, Calender):
    pass 
class OrganisedBaby(Baby, Calender):
    pass 

andres = OrganisedAdult("Andre", "Gomez") 
boris = OrganisedBaby("Boris", "Bumble")
andres.speak() 
boris.book_appointment(datetime.date(2018, 1, 1))
