#Types of Inheritance in Python
#Single Inheritance → One parent, one child.
class Animal:
    def eat(self):
        print("Animal eats food")
class dog(Animal):   # dog inherites from animal
    def bark(self):
        print("dog barks")        
d=dog()      
d.eat()  # eat interited from animal
d.bark() # dog own method

#Multiple Inheritance → Child inherits from multiple parents.
class father:
    def speak(self):
        print("father speaks")
class mother:
    def cook(self):
        print("mother cooks")
class child(father,mother):
    def play(self):
        print("child plays")
c=child()
c.speak()
c.cook()
c.play()        


#Multilevel Inheritance → Chain of inheritance.
#Grandparent → Parent → Child
class grandparent:
    def speak(self):
        print("grandparent speaks")
class parent(grandparent):  # parent inherites from grand parent
    def cook(self):
        print("parent cooks")        
class child(parent):  # child inherites from parent
    def play(self):
        print("child plays")
c=child()        
c.speak() # from grandparent
c.cook()  #from parent
c.play()  # frrom child 


#Hierarchical Inheritance → One parent, many children.
#        Parent
    #   /   |   \
# Child1  Child2 Child3

class Parent:
    def house(self):
        print("Parent owns a house ")

class Son(Parent):   # inherits from Parent
    def bike(self):
        print("Son rides a bike ")

class Daughter(Parent):  # inherits from Parent
    def car(self):
        print("Daughter drives a car ")

# Usage
s = Son()
s.house()   # from Parent
s.bike()    # Son’s own method

d = Daughter()
d.house()   # from Parent
d.car()     # Daughter’s own method

#Hybrid Inheritance → Combination of above types.
#Hybrid Inheritance is a combination of two or more types of inheritance (single, multiple, multilevel, hierarchical) in a single program
# Base class
class Grandparent:
    def house(self):
        print("Grandparent owns a house 🏠")

# Parent1 inherits from Grandparent (Multilevel part)
class Parent1(Grandparent):
    def car(self):
        print("Parent1 owns a car 🚗")

# Parent2 (another parent, for multiple inheritance)
class Parent2:
    def land(self):
        print("Parent2 owns land 🌳")

# Child inherits from Parent1 and Parent2 (Multiple + Multilevel)
class Child(Parent1, Parent2):
    def bike(self):
        print("Child rides a bike 🚲")

# Usage
c = Child()
c.house()  # from Grandparent
c.car()    # from Parent1
c.land()   # from Parent2
c.bike()   # Child’s own method
