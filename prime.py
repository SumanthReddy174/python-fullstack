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

