#variables-a variable is a name given in memory location in program
name="jhon"
age=23
height=6.1
print("My name is:",name)
print("My age is:",age)
print("height is:",height)

#2 simple

a = 10
b = 20
c = a + b
print("Sum:", c)

#3Dynamic typing example can change their type easily.

x = 10
print(x, type(x))

x = "Hello"
print(x, type(x))

x = 3.5
print(x, type(x))

#add

a = 5
b = 8
sum = a + b
print("Sum:", sum)

#4 Swap two variables
x = 10
y = 20

x, y = y, x   # swapping values
print("x =", x)
print("y =", y)

#5 Calculate area of a rectangle
length = 10
breadth = 5
area = length * breadth
print("Area of Rectangle:", area)

#6 Store and print your details
name = "Sumanth"
age = 21
college = "ABC College"
print("Name:", name)
print("Age:", age)
print("College:", college)

#7 Calculate average of three numbers
a = 10
b = 20
c = 30
average = (a + b + c) / 3
print("Average:", average)
#7 Convert temperature (Celsius → Fahrenheit)
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#Calculate simple interest
p = 1000  # principal
r = 5     # rate
t = 2     # time

si = (p * r * t) / 100
print("Simple Interest:", simple)

# Find perimeter and area of a circle
pi = 3.14159
radius = 7
perimeter = 2 * pi * radius
area = pi * radius * radius

print("Perimeter:", perimeter)
print("Area:", area)

# Demonstrate variable reassignment
x = 100
print("x =", x)

x = "Python"
print("x =", x)

x = 3.14
print("x =", x)

 #Calculate student total and average marks
sub1 = 80
sub2 = 90
sub3 = 85
sub4 = 75
sub5 = 95

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5

print("Total Marks:", total)
print("Average Marks:", average)

#HARD LEVEL PROGRAMS
# Using variables in an expression
a = 5
b = 3
c = 2

result = (a ** b) + (b * c) - (a / c)
print("Result:", result)

# Combine string variables
first_name = "Sumanth"
last_name = "Reddy"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Calculate compound interest
p = 5000
r = 5
t = 3

amount = p * (1 + r/100)**t
ci = amount - p

print("Compound Interest:", ci)

# Convert minutes into hours and minutes
minutes = 135
hours = minutes // 60
remaining_minutes = minutes % 60

print(hours, "hours and", remaining_minutes, "minutes")

 #Simple calculator using variables
a = 10
b = 5

add = a + b
sub = a - b
mul = a * b
div = a / b

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)


# data types
#A data type defines the kind of value a variable can hold and what operations can be performed on it.
# data types in python
#1 int
#2float
#3 str
#4 bool
#5 list
#6 tuple
#7 dict
#8 set
#9 complex
#10 none type
#integer
Integer (int)
a = 10
b = -25
print(a, type(a))
print(b, type(b))



# Float (float)
x = 3.14
y = -9.8
print(x, type(x))
print(y, type(y))

# String (str)
name = "Sumanth"
greeting = 'Hello'
print(name, type(name))
print(greeting, type(greeting))

# Boolean (bool)
is_student = True
is_teacher = False
print(is_student, type(is_student))
print(is_teacher, type(is_teacher))

# List (list)
fruits = ["apple", "banana", "mango"]
print(fruits, type(fruits))


# Lists are mutable (can be changed):

fruits[1] = "grapes"
print(fruits)

# Tuple (tuple)
numbers = (1, 2, 3, 4)
print(numbers, type(numbers))


# Tuples are immutable (cannot change values):

# numbers[0] = 10   # ❌ will cause error

# Set (set)
colors = {"red", "green", "blue"}
print(colors, type(colors))


# Sets remove duplicates automatically:

nums = {1, 2, 2, 3, 3, 4}
print(nums)

#Dictionary (dict)
student = {"name": "Sumanth", "age": 21, "course": "CSE"}
print(student, type(student))
print(student["name"])

#Complex Number (complex)
z = 2 + 3j
print(z, type(z))
print("Real part:", z.real)
print("Imaginary part:", z.imag)

# NoneType
x = None
print(x, type(x))

 Bonus: Use type() and isinstance()
x = 10
print(type(x))              # Shows the type
print(isinstance(x, int))   # Checks if x is int