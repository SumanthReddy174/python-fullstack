#An operator is a symbol that performs an operation on one or more values (operands).
#| Type                                  | Description                       | Example                                         |                         
#| ------------------------------------- | --------------------------------- | ----------------------------------------------- |
# 1️⃣ Arithmetic Operators              | Perform mathematical operations   | `+`, `-`, `*`, `/`, `%`, `//`, `**`             |                         
# 2️⃣ Comparison (Relational) Operators | Compare two values                | `==`, `!=`, `>`, `<`, `>=`, `<=`                |                         
# 3️⃣ Assignment Operators              | Assign values to variables        | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `**=`, `%=` |                         
# 4️⃣ Logical Operators                 | Combine conditional statements    | `and`, `or`, `not`                              |                         
# 5️⃣ Bitwise Operators                 | Work on bits (0s and 1s)          | `&`, `                                          |  
# 6️⃣ Identity Operators                | Compare memory locations          | `is`, `is not`                                  |                         
# 7️⃣ Membership Operators              | Test for membership in a sequence | `in`, `not in`                                  |                         

#programs
#Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division (float)
print(a // b)  # Floor division
print(a % b)   # Modulus (remainder)
print(a ** b)  # Exponent (power)



# Comparison (Relational) Operators
x = 5
y = 10

print(x == y)   # Equal
print(x != y)   # Not equal
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater than or equal
print(x <= y)   # Less than or equal



#Assignment Operators
a = 10
a += 5   # same as a = a + 5
print(a)

a -= 3   # a = a - 3
print(a)

a *= 2   # a = a * 2
print(a)

a /= 4   # a = a / 4
print(a)

a //= 2  # a = a // 2
print(a)

# Logical Operators
x = True
y = False

print(x and y)  # True if both are True
print(x or y)   # True if one is True
print(not x)    # Reverses True → False




#Bitwise Operators (work at binary level)



a = 5   # (binary 0101)
b = 3   # (binary 0011)

print(a & b)   # AND
print(a | b)   # OR
print(a ^ b)   # XOR
print(~a)      # NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right 

#Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same object)
print(x is z)      # False (different objects)
print(x is not z)  # True

# Membership Operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True


#type conversion 
#| Function  | Converts To    | Example                      |
#| --------- | -------------- | ---------------------------- |
#| `int()`   | Integer        | `int(3.8)` → `3`             |
#| `float()` | Floating point | `float(5)` → `5.0`           |
#| `str()`   | String         | `str(10)` → `'10'`           |
#| `bool()`  | Boolean        | `bool(0)` → `False`          |
#| `list()`  | List           | `list((1,2,3))` → `[1,2,3]`  |
#| `tuple()` | Tuple          | `tuple([1,2,3])` → `(1,2,3)` |
#| `set()`   | Set            | `set([1,2,2,3])` → `{1,2,3}` |

# programs 
#int() → convert to integer
a = "10"
b = int(a)
print(b, type(b))

#float() → convert to float
a = "3.14"
b = float(a)
print(b, type(b))

#str() → convert to string
a = 25
b = str(a)
print(b, type(b))

# list(), tuple(), set()
t = (1, 2, 3)
l = list(t)
s = set(t)

print(l, type(l))
print(s, type(s))

#Convert int to bool
a = 0
b = 5
print(bool(a))  # False
print(bool(b))  # True

# Mixed type example
x = "50"
y = 10

# Convert string to int before addition
sum = int(x) + y
print(sum)