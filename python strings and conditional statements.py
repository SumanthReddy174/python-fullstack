#strings :-string is a data type that stores a sequence of characters.
#strings are enclosed in either single quotes or double quotes.
#strings are immutable, which means that once a string is created it cannot be changed or modified 
#strings can be concatenated using the + operater
#strings can be repeated using the * operater.
#strings can be indexed and sliced using square brackets []
#strings programs 

#1 string concatenation 
str1="sumanth"
str2="reddy"
str3=str1+str2
print(str3)
#2
str1="hello"
str2="world"
sum=str1+str2
print(sum)

#3
str1="bike"
str2="car"
str3=str1+" "+str3
print(str3)

# length of string
str1="sumanthreddy"
len1=len(str1)
print(len1)


# indexing of string
str1="python"
print(str1[0])
print(str1[1])

#2
str1="programing"
print(str1[3])
print(str1[5])

#3
str1="developer"
print(str1[2])

# string slicing
#string slicing is used to extract a sub string from astring.
#string slicing is done using the square brackets []and the colon :
# the sytax for string slicing is string [start:end]
#1
str1="python programming"
print(str1[0:6])
print(str1[7:18])

#2
str1="cars are fast"
print(str1[0:4])

#3
text = "Python"
print(text[:4])   # from beginning to index 3
print(text[2:])   # from index 2 to end


#4
text = "ABCDEFG"
print(text[::2])   # take every 2nd letter

#5
text = "Python"
print(text[::-1])

#6
text = "I love Python"
print(text[2:6])

#7
 #P   y   t   h   o   n
 #0   1   2   3   4   5
#-6  -5  -4  -3  -2  -1

text = "Python"
print(text[-4:-1])

# summary
#| Slice        | Meaning             | Example Output (text = "Python") |
#| ------------ | ------------------- | -------------------------------- |
#| `text[0:3]`  | from index 0 to 2   | Pyt                              |
#| `text[:4]`   | from start to 3     | Pyth                             |
#| `text[2:]`   | from index 2 to end | thon                             |
#| `text[-3:]`  | last 3 characters   | hon                              |
#| `text[::-1]` | reverse string      | nohtyP                           |
#| `text[::2]`  | every 2nd letter    | Pto                              |

#string functions
#String functions are built-in methods in Python used to perform different operations on strings 
# — like changing case, finding text, replacing words, etc.
# 1 upper() – Converts all letters to UPPERCASE
text = "hello"
print(text.upper())


# lower() – Converts all letters to lowercase
text = "HELLO"
print(text.lower())




# title() – Makes the first letter of every word uppercase
text = "python is fun"
print(text.title())



# capitalize() – Makes only the first letter of the sentence uppercase
text = "python is fun"
print(text.capitalize())



# swapcase() – Changes upper to lower and lower to upper
text = "PyThOn"
print(text.swapcase())



# len() – Returns the length (number of characters)
text = "Python"
print(len(text))

# strip() – Removes spaces from start and end
text = "   hello   "
print(text.strip())




# replace(old, new) – Replaces one part with another
text = "I like Java"
print(text.replace("Java", "Python"))



#count(substring) – Counts how many times a word or letter appears
text = "banana"
print(text.count("a"))

# find(substring) – Finds the first index of the word
text = "Hello World"
print(text.find("World"))



# index(substring) – Same as find() but gives error if not found
text = "Hello"
print(text.index("H"))  # Works fine
# print(text.index("z"))  # ❌ Error

# startswith() – Checks if string starts with something
text = "Python Programming"
print(text.startswith("Python"))



#endswith() – Checks if string ends with something
text = "Python Programming"
print(text.endswith("Programming"))




# split() – Splits string into a list
text = "I love Python"
print(text.split())




# join() – Joins list elements into one string
words = ['I', 'love', 'Python']
print(" ".join(words))



#isdigit() – True if all characters are digits
num = "1234"
print(num.isdigit())



#isalpha() – True if all are alphabets
text = "Python"
print(text.isalpha())

# isalnum() – True if all are letters or numbers
text = "Python123"
print(text.isalnum())


#isspace() – True if string has only spaces
text = "   "
print(text.isspace())



# center(width, char) – Centers the text
text = "Python"
print(text.center(10, '*'))


# conditonal statements 
#In Python, conditions are checked using if, elif, and else.
#1
#Example 1: Simple if Statement
age = 18

if age >= 18:
    print("You can vote ✅")
#2
#if-else Statement
age = 15

if age >= 18:
    print("You can vote ✅")
else:
    print("You cannot vote ❌")   

#3 if elif else statement
marks = 85

if marks >= 90:
    print("Grade: A+ 🏆")
elif marks >= 75:
    print("Grade: A 🎉")
elif marks >= 60:
    print("Grade: B 👍")
else:
    print("Grade: C 👌")

#4  nested if 
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You can vote ✅")
    else:
        print("You must be a citizen to vote")
else:
    print("You are too young to vote ❌")
# 6 logical operaters
#Using Logical Operators

#You can combine conditions using:

#and → both must be True

#or → at least one must be True

#not → reverses True/False

age = 19
has_id = True

if age >= 18 and has_id:
    print("You can enter the club 🎉")
else:
    print("You cannot enter 🚫")#   

#| Keyword | Meaning                                    | Example               |
#| ------- | ------------------------------------------ | --------------------- |
#| `if`    | Checks a condition                         | `if x > 0:`           |
#| `elif`  | Checks next condition if previous is False | `elif x == 0:`        |
#| `else`  | Runs if all conditions are False           | `else:`               |
#| `and`   | Both must be True                          | `if x > 0 and y > 0:` |
#| `or`    | At least one True                          | `if x > 0 or y > 0:`  |
#| `not`   | Reverses condition                         | `if not x > 0:`       |

