num = 7

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
#2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
print("Prime" if is_prime(num) else "Not Prime")  
#3
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num) 
#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
print("Prime" if is_prime(num) else "Not Prime")       


#5
num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")
else:
    i = 2
    while i < num:
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")
#6
import math

num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
#7
n = int(input("Enter number: "))
print("Prime" if n > 1 and all(n % i != 0 for i in range(2, n)) else "Not Prime")        
