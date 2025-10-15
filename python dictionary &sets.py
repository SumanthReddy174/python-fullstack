#dictionary
#A dictionary is a collection of key-value pairs in Python.
#2️⃣ Each item has a key and a value: key: value.
#3️⃣ Dictionaries are written using curly braces { }.
#4️⃣ Example: student = {"name": "Sumanth", "age": 21}
#5️⃣ Dictionary items are unordered, so they do not have a fixed index.
#6️⃣ Keys must be unique, but values can be repeated.
#7️⃣ Dictionaries are mutable, meaning you can change, add, or remove items.
#8️⃣ Access values using their keys: student["name"] → "Sumanth"
#9️⃣ Common methods: keys(), values(), items(), get(), pop().
#🔟 Dictionaries are very useful for storing data in a structured way.
#create of dictionary
#1
student = {"name": "Sumanth", "age": 21, "city": "Hyderabad"}
print(student)


#1️⃣ Create and Print a Dictionary
student = {"name": "Sumanth", "age": 21, "city": "Hyderabad"}
print(student)

# 2️⃣ Access Value by Key
print(student["name"])  # Sumanth
print(student.get("age"))  # 21

# 3️⃣ Add a New Key-Value Pair
student["grade"] = "A"
print(student)

# 4️⃣ Update a Value
student["age"] = 22
print(student)

# Remove a Key-Value Pair
student.pop("city")
print(student)

# Remove Last Item
student.popitem()
print(student)

# Loop Through Keys
for key in student:
    print(key)

#Loop Through Values
for value in student.values():
    print(value)

#Loop Through Key-Value Pairs
for key, value in student.items():
    print(key, ":", value)

#Check if Key Exists
if "name" in student:
    print("Name is present")

# Dictionary Length
print(len(student))

# Merge Two Dictionaries
student2 = {"hobby": "coding", "age": 23}
student.update(student2)
print(student)

#Clear Dictionary
student.clear()
print(student)

# Nested Dictionary
students = {
    "s1": {"name": "Sumanth", "age": 21},
    "s2": {"name": "Reddy", "age": 22}
}
print(students)

# Get Keys and Values Separately
print(students.keys())
print(students.values())

#Convert Two Lists into a Dictionary
keys = ["name", "age", "city"]
values = ["Sumanth", 21, "Hyderabad"]
my_dict = dict(zip(keys, values))
print(my_dict)

# Count Frequency of Characters
text = "hello"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)



# Find Max Value in Dictionary
marks = {"Math": 90, "Science": 85, "English": 95}
max_subject = max(marks, key=marks.get)
print(max_subject, marks[max_subject])

# Sort Dictionary by Key
marks = {"Math": 90, "Science": 85, "English": 95}
for key in sorted(marks):
    print(key, ":", marks[key])

# Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)




#dictionary methods

#keys() → Returns all keys
student = {"name": "Sumanth", "age": 21, "city": "Hyderabad"}
print(student.keys())




# values() → Returns all values
print(student.values())



#items() → Returns all key-value pairs
print(student.items())




# get(key) → Returns the value of a key
print(student.get("name"))   # Sumanth
print(student.get("grade", "Not Found"))  # gives default message if key missing

# update() → Adds or updates items
student.update({"age": 22, "grade": "A"})
print(student)



# pop(key) → Removes item by key
student.pop("city")
print(student)



# popitem() → Removes last inserted item
student.popitem()
print(student)

# clear() → Removes all items
student.clear()
print(student)



# copy() → Returns a copy of the dictionary
student = {"name": "Sumanth", "age": 21}
new_student = student.copy()
print(new_student)

# fromkeys() → Creates a new dictionary from keys
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "unknown")
print(new_dict)



#setdefault() → Returns value of key; adds key if not found
student = {"name": "Sumanth"}
student.setdefault("age", 21)
print(student)



# len() → Returns total number of items
student = {"name": "Sumanth", "age": 21}
print(len(student))



# del keyword → Deletes an item or entire dictionary
del student["age"]
print(student)

#in keyword → Checks if a key exists
student = {"name": "Sumanth", "age": 21}
print("name" in student)  # True
print("grade" in student) # False

# Loop through Dictionary
for key, value in student.items():
    print(key, ":", value)




#sets
#Unordered → Items don’t have a fixed position or index.
# No duplicates → Repeated values are removed automatically.
#Mutable → You can add or remove items.
#Unindexed → You can’t access elements by index like lists.
#Created using {} or set() function.
# Can store different data types (int, string, etc.).
#Supports mathematical set operations like union, intersection, etc.
# Cannot contain mutable items (like lists or dictionaries).
# Very useful for removing duplicates.
# Fast for membership testing (in keyword).


#1
#Create a Set
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Remove Duplicates Automatically
nums = {1, 2, 2, 3, 4, 4}
print(nums)



# Create Empty Set (use set(), not {})
empty_set = set()
print(type(empty_set))

# Add Element
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)

# Add Multiple Elements
fruits.update(["orange", "mango"])
print(fruits)

# Remove an Element
fruits.remove("banana")
print(fruits)

# Discard an Element (no error if missing)
fruits.discard("grapes")  # no error even if 'grapes' not found
print(fruits)

# Pop (Removes random item)
item = fruits.pop()
print("Removed:", item)
print(fruits)

#Clear the Set
fruits.clear()
print(fruits)

# Delete Entire Set
numbers = {1, 2, 3}
del numbers

# Set Operations
# Union → Combines all items (no duplicates)
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))



# Intersection → Common items only
print(a.intersection(b))



# Difference → Items in a but not in b
print(a.difference(b))



#Symmetric Difference → Items not common in both
print(a.symmetric_difference(b))
