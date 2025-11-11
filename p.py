def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)  
print(factorial(5))        


#2

def sum_of_naturals(n):
    if n==1:
        return 1
    else:
        return n + sum_of_naturals(n-1)
print(sum_of_naturals(5))

#3 
def print_numbers(n):
    if n==0:
        return
    else:
          
        print_numbers(n-1)
        print(n)
        
print_numbers(5)        

#4
students = {
    101: {"name": "Ravi", "age": 20},
    102: {"name": "Sumanth", "age": 21}
}

print(students[101]["name"])  # Ravi

# Add nested
students[103] = {"name": "Anjali", "age": 19}
print(students)






   



    




