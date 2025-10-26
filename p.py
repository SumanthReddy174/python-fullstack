#1
def multiply(a,b):
    return a * b
result = multiply(3,4)
print("result:", result)

#2
def greet(name):
    print("hallo",name)
greet("Alice")  

#3
def student(name,age,id):
    print("Name:",name)
    print("Age:",age)
    print("Id:",id)

student("bob",45,"h56")

# 4
def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial:", factorial (5))
