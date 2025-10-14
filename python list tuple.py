#lists in python 
#lists are built in datatypes that stores the set of values
#list is denoted as []
#List is a collection of multiple items stored in a single variable.
# Example: fruits = ["apple", "banana", "cherry"]

# Lists are written using square brackets [ ].
👉 Example: numbers = [1, 2, 3, 4]

# List items are ordered, meaning each item has a fixed position (index).
👉 Example: Index of "apple" is 0 in ["apple", "banana", "cherry"].

# Lists are mutable — you can change, add, or remove items anytime.
👉 Example:

fruits[1] = "mango"


# Lists can store different data types (int, float, string, bool).
👉 Example: [10, "Hello", 3.5, True]

# Lists allow duplicate values.
👉 Example: [1, 2, 2, 3]

# You can access items using index numbers (starting from 0).
👉 Example:

fruits = ["apple", "banana"]
print(fruits[0])  # apple


#Use list methods like:
append(), insert(), remove(), pop(), sort(), reverse().

#Use len() to find number of items in a list.
👉 Example: len(fruits) → gives 3.

# Lists can be looped using a for loop.
#Example:

for x in fruits:
    print(x)

 # programs
# Accessing List Items (Using Index)

#Indexes start from 0.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
print(fruits[2])  # cherry




# Negative Indexing

#Negative index means counting from the end.

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # cherry
print(fruits[-2])  # banana

#Slicing Lists

#You can get a part (slice) of a list.

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # from index 1 to 3




# Changing List Items

#Lists are mutable, meaning you can change their values.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)



#Adding Items to a List
# append() → Adds item at the end
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)



# insert() → Adds item at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "mango")
print(fruits)



# extend() → Adds another list to the current one
a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)

# remove() → Removes by value
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)



# pop() → Removes by index
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)



#del → Deletes item or whole list
numbers = [1, 2, 3, 4]
del numbers[2]
print(numbers)



# clear() → Removes all items
numbers = [1, 2, 3]
numbers.clear()
print(numbers)



# Looping Through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruits)
  
# sorting list
list=[3,1,2,4]
list.sort()
print(list)

# tuple
#Tuple is a collection of multiple items stored in a single variable — just like a list.
# Example:

fruits = ("apple", "banana", "cherry")


# Tuples are written using round brackets ( ), not square ones.
# Example: numbers = (1, 2, 3, 4)

# Tuple items are ordered, meaning they have fixed positions (index starts at 0).
# Example:

print(fruits[0])  # apple


# Tuples are immutable, meaning you cannot change, add, or remove items after creation.
# Example:

my_tuple = (1, 2, 3)
# my_tuple[1] = 5 ❌  # Not allowed


# Tuples can store different data types (int, float, string, etc.).
# Example:

info = ("Sumanth", 20, 3.9, True)


# Tuples allow duplicate values.
# Example:

numbers = (1, 2, 2, 3)


# You can access items using indexes, just like in lists.
# Example:

print(numbers[1])  # 2


# Use len() to find how many items are in a tuple.
# Example:

print(len(numbers))  # 4


# You can loop through a tuple using a for loop.
# Example:

for x in fruits:
    print(x)
 #programs
 # Create and Print a Tuple
fruits = ("apple", "banana", "cherry")
print(fruits)



# Access Elements in a Tuple
colors = ("red", "green", "blue")
print(colors[0])  # red
print(colors[2])  # blue

# Find the Length of a Tuple
numbers = (10, 20, 30, 40)
print("Length:", len(numbers))



#Check if an Item Exists
animals = ("cat", "dog", "cow")
if "dog" in animals:
    print("Yes, dog is in the tuple")




# Tuple Slicing
numbers = (1, 2, 3, 4, 5, 6)
print(numbers[1:4])   # from index 1 to 3
print(numbers[:3])    # from start to 2
print(numbers[-3:])   # last 3 elements



# Concatenate Two Tuples
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)




# Repeat a Tuple
fruits = ("apple", "banana")
print(fruits * 3)


# Find Maximum and Minimum Values
numbers = (10, 25, 5, 40)
print("Max:", max(numbers))
print("Min:", min(numbers))




# Count Occurrences of an Item
numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))



# Find Index of an Item
names = ("Sumanth", "Reddy", "Python")
print(names.index("Python"))



#2
marks = (85, 90, 78, 92)
for m in marks:
    print("Mark:", m)