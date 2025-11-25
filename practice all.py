num=-10
if num>0:
    print("positive number")
#2
num = -10

if num > 10:
    print("Positive")
elif num < 10:
    print("Negative")
else:
    print("Zero")



#3
name="bob"
if name=="alice":
    print("hello,alice")
elif name=="bob":
    print("hello ,bob")
else:
    print("hello,guest")

#4
age=-30
if age<30:
   if age<30: 
    print("minor")
   else:
        print("adult")    
else:
    print("non-positive number")


#5
age=17
salary = 25000
if age >18 and salary >= 20000:
    print("eligible for loan")
else:
     print("not eligible for loan")    

#6
day= "monday"
if day=="saturday"or day=="sunday":
    print("its weed end")
else:
    print("its not aweekend ")  

#7
vechile="bike"
if vechile=="bike" or vechile=="scooty":
    print("two wheeeler")
else:
    print(" four wheeler")

#8
cloths="t-shirt"
if cloths == "t-shirt" or cloths == "jeans":
    print("casual wear")
else:
    print("formal wear")
#9
number=17
if  number % 2 == 0:
    print("even number")
else:
    print("odd num")

#10
marks=90
if marks >= 90:
    print("grade A")

elif marks >= 80:
    print("grade B")
else:
    print("grade C")
#11 
status = True
if not status:
    print(" studying") 
else:
    print(" not studying")
#12
year=2020
if (year%4==0 and year%100 !=0) or (year%400==0):
    print(year,"leap year")
else:
    print(year,"not a leap year") 
# lambda function 
#1
square =lambda x: x*x
print(square(5))
#2
add= lambda a,b: a+b
print(add(4,8))
#3
max_lambda= lambda a, b: a if a>b else b
print(max_lambda(10,20))
#4
factorial= lambda n: 1 if n==0 else n*factorial(n-1)
print(factorial(5))
#6
reverse_string= lambda a: a[::-1]
print(reverse_string("hello"))
#7
is_even= lambda x: "Even" if x%2==0 else "odd"
print(is_even(2))
#8
cube= lambda x: x**3
print(cube(3))

# 9
students= [("sumanth",20),("arun",45),("ravi",17)]
students.sort(key=lambda x: x[1])
print(students)

#10
nums =[10,20,30,40,50,60]
squares=list(map(lambda x: x*x, nums))
print(squares)
#11
nums=[1,2,3,4,5,6,7]
evens=list(filter(lambda x:x%2==0, nums))
print(evens)
#12
from functools import reduce
nums=[1,2,3,4,5]
product= reduce(lambda x,y :x*y, nums)
print(product)
#13
length= lambda s: len(s)
print(length("hello world"))
#14
add_five= lambda x: x+5
print(add_five(10))
#15
to_upper=lambda x: x.upper()
print(to_upper ("sumanth"))
#16
is_palindrome= lambda s: s==s[::-1]
print(is_palindrome("madam"))
#17
max_of_three= lambda a,b,c: a if (a<b and a<c ) else (b if b<c else c)
print(max_of_three(10,20,5))
#18
area_circle= lambda r: 3.14*r*r
print(area_circle(5))
#19
fahrenheit_to_celsius= lambda f: (f-32)*5/9
print(fahrenheit_to_celsius(98))
#20
is_owel= lambda c: c.lower() in 'aeiou'
print(is_owel('b'))
#21
concat= lambda a,b : a+b 
print(concat("hello","world"))
#22
square_root= lambda x: x**0.5
print(square_root(16))
#23 file handling
file = open("example.txt","w")
file.write("hello world\n")
file.close()
print("file created successfully")
#1
file = open("example.txt","r")
content = file.read()
file.close()
print(content)
#2
file= open("example.txt","a")
file.write("welcome to file handling\n")
file.close()
print("successfully")
#3
file=open("example.txt","r")
lines=file.readlines()
for line in lines:
    print(line.strip())
    file.close()
#4
file=open("example.txt","w")
file.write("this file is created using python\n")
file.write("file handling is easy\n")
file.close()
print("file overwritten successfully")
#5
file=open("example.txt","r")
content=file.read()
print("file content:")
print(content)
file.close()
#6
file=open("example.txt","a")
file.write("appending  new line to the file\n")
file.close()
print("line appended successfully")
#7
file=open("example.txt","r")
lines=file.readlines()
for line in lines:
    print(line.strip())
    file.close()
#8
file=open("example.txt","r+")
content=file.read()
print("file content before modification:")
print(content)
file.write("adding new content to the file\n")
file.close()
print("file modified ")
 # functions
 # 1
def greet():
    print("hello,world") 
greet()
#2
def add(a,b):
    print("sum","result",a+b)
add(5,10)    
#3
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#4
def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(4))
#5
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(10)
#6
def square(num):
    return num*num
print(square(7))
#7
def reverse_string(a):
    return a[::-1]
print(reverse_string("python"))
#8
def max_of_two(a,b):
    print(a if a>b else b)
max_of_two(10,20)
#9
def is_palindrome(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
is_palindrome("madam")
#10
def student(Name,Age):
    print("Name:",name)
    print("age:",age)
student("sumanth",21)
#11
def areaof_circle(r):
    pi=3.14
    area=pi*r*r
    return area
print(areaof_circle(5))
#12
def celusius_to_fahrenheit(c):
    f=(c*9/5)+32
    return f
print(celusius_to_fahrenheit(37))
#13
def show_numbers(*nums):
    print("numbers:",nums)
show_numbers(1,2,3,4,5)
#14
def factorial_iterate(n):
    result=1
    for i in range(1,n+1):
        result *=i
        return result
print(factorial_iterate(5))
#15
def add_numbers(*args):
    return sum(args)
print(add_numbers(1,2,3,4,5,6,7,8))
#kwargs
#1
def details(**info):
    for key, value in info.items():
        print(key, ":", value)

details(name="Sumanth", age=21, course="Python")
#2
def display(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
display(city="new york", country="usa", population=81228889)
#3
def profile(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} -> {value}") 
profile(name="alice", age=30, profession="engineer")
#4
def students(**info):
    for key , value in info.items():
        print(f"{key} = {value}")
students(name="bob", age=25,major="math")
#5
def car_details(**detials):
    for key , value in detials.items():
        print(f"{key } = {value}") # we have to use f string to print key and values  
car_details(make="toyota",model="coralla",year=2026)
#6
def book_info(**info):
    for key , value in info.items():
        print(f"{key}: {value}")
book_info(title="story of python", author="john doe",pages=350)
#7
def empolyee_data(**data):
    for key ,value in data.items():
        print(f"{key} -> {value}")
empolyee_data(name="sumanth", id=101, deparment="IT")
#8
def country_info(**details):
    for key , value in details.items():
        print(f"{key}={value}")
country_info(name="india", capital="new delhi", population=122223)
#9
def laptop_specs(**specs):
    for key , value in specs.items():
        print(f"{key} : {value}")
laptop_specs(brand="dell", model="xp", ram="16gb")
#10
def movie_details(**info):
    for key , value in info.items():
        print(f"{key} - {value}")
movie_details(title= "inception", direction="nolan", year=2025)
#11
def city_data(**data):
    for key , value in data.items():        
       print(f"{key} -> {value}")
city_data(name="paris", country="france", pop =100000)
#12
def phone_specs(**specs):
    for key , value in specs.items():
        print(f"{key} : {value}")
phone_specs(brand="apple", model="iphone 17", storage="256gb")
# error and expections
#1
#try:
#    num = int(input("enter a number: "))
#   result = num/0
#    print("result;", result)
#except ZeroDivisionError:
#    print("error: division by zero is not allowed")
#2 
try:
    file = open("non_extensive_file.txt", "r")
except FileNotFoundError:
    print("error: file not found")
#3
#try :
 #   num = int(input("enter a number:"))
  #  print("you entered:",num)
#except ValueError:
#    print("error : invalide input , give correct input")
#4
try:
    a=10
    b=20
    result = a+b
    print("result:",result)
except Exception as e:
 print("an error occured:",e)
#5
try:
    lst =[1,2,3,4,5]
    print(lst[10])
except IndexError:
    print("error: index out of range")
#6
try:
    num = int(input("enter a number: "))
    reciporcal = 1/num
    print("reciporcal:,reciporcal")
except ZeroDivisionError:
    print("error: division by zero is not allowed")
except ValueError:
    print("error: invalid input , please enter a valid number")
#7 
try:
    dictionary = {"a": 1, "b": 2, "c":3}
    print(dictionary["d"])
except KeyError:
    print("error: key not found in dictionary")
#8
try:
    num = int(input("enter a number: "))
    result = 100/num
    print("result:",result)
except ZeroDivisionError:
    print("error: division ny zero is not allowed")
except ValueError:
    print("error: invalid input , please enter valid input")
#9
try:
    result = 10 + "5"
    print("result:,result")    
except TypeError:
    print("error: unsupported operand type(s) for +")
#10
try:
    file = open("example.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("error: file not found")
#11
try:
    num = int(input("enter a number: "))
    print("you entered:",num)
except ValueError:
    print("error: invalid input , please enter a valid number")
#12
try:
    lst=[1,2,3]
    print(lst[5])
except IndexError:
    print("error: index out of range")
#13
try:
    result=10/0
    print("result:",result)
except ZeroDivisionError:
    print("eroor: division by zero is not allowed")
#14
try:
    dictionary={"x":10,"y":20} 
    print(dictionary["z"])
except KeyError:
    print("error: key not found in dictionary") 
#15
try:
    num = int(input("enter a number:"))
    reciporcal = 1/num
    print("reciporcal:",reciporcal)
except ZeroDivisionError:
    print("error: division by zero is not allowed")
except ValueError:
    print("error: invalid input, please enter a valid number")
#16
try:    
    result ="hello world" + 5
    print("result:",result)
except TypeError:
    print("error: unsupported operand type(s) for +") 

#17
try:
    file = open("data.txt","r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("error: file not found")
#18
try:
    num = int(input("enter a number:"))
    print("you entered",num)      
except ValueError:
    print("error: invalid input,please enter a valid number")
#19
try:
    lst =[1,2,3]
    print(lst[10])
except IndexError:
    print("error: index out of range")
    #20
try:
    result =10/0
    print("result:",result)
except ZeroDivisionError:
    print("error: division by zero is not allowed")
    




            
               
    



            
       

            

          

    



    





    




    








         
























               





















    










