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
#8
num = int(input("Enter number: "))

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")
#9
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "Prime")
#10
count = 0

for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1

print("Total primes:", count)
#11
try:
    num = int(input("Enter number: "))
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        if num > 1:
            print("Prime")
        else:
            print("Not Prime")
except:
    print("Enter valid number")
#12
num = int(input("Enter number: "))

if num == 2 or num == 3:
    print("Prime")
elif num % 2 == 0 or num <= 1:
    print("Not Prime")
else:
    print("Prime")
#13
num = int(input("Enter number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime")
else:
    print("Not Prime")
#14
count = 0
num = 2

while count < 10:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1

#15
num = int(input("Enter number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    if num > 1:
        print("Prime")
    else:
        print("Not Prime")
#16
num = int(input("Enter number: "))

if num % 2 == 0 and num != 2:
    print("Even and Not Prime")
elif num == 2:
    print("Even Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Odd and Not Prime")
            break
    else:
        print("Odd Prime")
#17
def check_prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return check_prime(n, i+1)

num = int(input("Enter number: "))
print("Prime" if check_prime(num) else "Not Prime")
#18
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, "Prime")
#19
def prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

num = int(input("Enter number: "))
print(prime(num))
#20
count = 0

for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1

print("Total primes:", count)
#21
try:
    num = int(input("Enter number: "))
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        if num > 1:
            print("Prime")
        else:
            print("Not Prime")
except:
    print("Enter valid number")
