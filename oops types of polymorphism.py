What is Polymorphism?

Polymorphism means "many forms".

In OOP, it allows the same function/method name to work in different ways depending on the object.

It makes code more flexible and reusable.

 Real-life example:

*The word "run" has many forms → a person runs, a car engine runs, a program runs.

Same action name, but different behavior.

🔹 Types of Polymorphism in Python

Method Overriding (runtime polymorphism)

A child class provides its own version of a method from the parent class.

Method Overloading (compile-time polymorphism)

Python does not support true overloading, but we can simulate it using default arguments or *args.

Operator Overloading

Using special methods (dunder methods) like __add__, __sub__, etc., we can change how operators work for our objects.

✅ Example 1: Polymorphism with Functions
def add(x, y, z=0):   # z is optional
    return x + y + z

print(add(2, 3))       # 5
print(add(2, 3, 4))    # 9


👉 Same function add() works in different ways.

✅ Example 2: Polymorphism with Classes
class Dog:
    def sound(self):
        print("Dog barks 🐶")

class Cat:
    def sound(self):
        print("Cat meows 🐱")

# Polymorphism: same method name "sound"
for animal in (Dog(), Cat()):
    animal.sound()




👉 Same method name, different behavior.

✅ Example 3: Method Overriding (Runtime Polymorphism)
class Bird:
    def fly(self):
        print("Most birds can fly ✈️")

class Penguin(Bird):
    def fly(self):   # overriding parent method
        print("Penguins cannot fly 🐧")

# Usage
b = Bird()
b.fly()

p = Penguin()
p.fly()



👉 Child overrides parent’s method.

✅ Example 4: Operator Overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overload + operator
    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(200)
print("Total Pages:", b1 + b2)




✅ Example 5: Polymorphism with len()
print(len("Hello"))      # string → 5
print(len([1, 2, 3, 4])) # list   → 4
print(len({"a": 1, "b": 2})) # dict → 2