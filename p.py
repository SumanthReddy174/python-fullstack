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
def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+ reverse_string(s[:-1])
print(reverse_string("sumanth"))
#5
text="sumanth reddy"
print(text.upper())




   



    




