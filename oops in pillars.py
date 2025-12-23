# Four pillars in oops
#1.encapsulation
#2.abstraction
#3.inheritance
#4.polymorphism

#Encapsulation:Encapsulation means hiding internal details of a class 
              #and only exposing what's necessary. It helps to protect important data 
              # from being changed directly and keeps the code secure and organized. 
class person:
    def __init__(self,name,age):
        self.__name=name  # private variable
        self.__age=age
    def display(self):# public method
        print("name:",self.__name)
        print("age:",self.__age)
p=person("sumanth",24) 
p.display() 

#Abstraction:Abstraction in Python's Object-Oriented Programming (OOP) is a fundamental concept that involves hiding complex 
# implementation details and showing only the essential features to the user. 
# It allows you to create a clear separation between what an object does and how it does it.

from abc import ABC, abstractmethod

class Remote(ABC):
    @abstractmethod
    def power(self):
        pass


class TV(Remote):
    def power(self):
        print("TV turned ON ")


class AC(Remote):
    def power(self):
        print("AC turned ON ")


# Usage
t = TV()
t.power()

a = AC()
a.power()

# Inheritance:one class (child) acquires the properties and methods of another class (parent).
class Animal:
    def eat(self):
        print("This animal eats food ")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks ")

# Usage
d = Dog()
d.eat()   # inherited from Animal
d.bark()  # Dog’s own method

# polymorphism:Polymorphism means "many forms".
#In OOP, it allows the same function/method name to work in different ways depending on the object.
#It makes code more flexible and reusable
class Bird:
    def fly(self):
        print("Some birds fly high")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

def show_flight(bird):
    bird.fly()

b1 = Bird()
p1 = Penguin()

show_flight(b1)
show_flight(p1)
