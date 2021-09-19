'''Keyword List'''
import keyword
# Print all keywords at once using "kwlist()"
print('The list of keywords is: ', keyword.kwlist)

'''True, False, None'''
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])

'''and, or, not, in, is'''
# and returns the first False value
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(3 and 0)
print(3 and 10)

# or returns first True value or last value if everything is false
print(3 or 10 or 30 or 10 or 70)
print(0 or False or 7 or 11)
print(0 or False)

# not inverts the truth value
print(not True)

# in used to check and loop through
str = 'I like ice cream'
if 'ice' in str:
    print('True', end=" ")
print('\r') # Creates new line

''' for and while'''
for s in str:
    print(s, end=" ")  # end=" " seperates each 's' and puts each iteration on the same line
print('\r')

# for used to control flow and looping
for i in 'I love you':
    print(i, end=" ")
print('\r')

# while similar to for loop
i = 0
while i < 10:
    # if i equals 7 increment by 1 and continue (skip 7)
    if i == 7:
        i += 1
        continue
    # print i
    else: 
        print(i, end=" ")
    # increment i so there is not an infinite loop
    i += 1 
print('\r')

'''return and yield'''
def fun():
    sum = 0
    # Create a list of numbers ranging from 0 to 9
    for i in range(10):
        # Get sum of i in loop ie. 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
        sum += i
    # Return sum 
    return sum
# Call fun() function
print(fun())

def fun():
    sum = 0
    for i in range(10):
        sum += i
        # yield returns a generator
        yield sum

for i in fun():
    print(i)

'''class'''
class Dog:
    # Attribute
    attr1 = 'mammal'
    attr2 = 'dog'

    # Method
    def aboutme(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

# Object instantiation
Money = Dog()

print(Money.attr2)
Money.aboutme()

'''as'''
# Create alias for module
import math as mt
print(mt.factorial(5))

'''pass'''
n = 10
for i in range(n):

    # pass can be used as placeholder
    # when code is to added later to prevent indention errors
    pass

'''Lambda'''
# Used to make inline returning functions with no statements allowed internally
g = lambda x: x * x * x
print(g(7))

'''Import and From'''
import math
print(math.factorial(7))

from math import factorial
print(factorial(4))

'''Exception Handling with try/catch/finally and assert'''
# try used to catch the errors in the code using the keyword except
# initializing number
a = 4
b = 0

try:
    # Raises divided by zero exception
    k = a//b
    print(k)
    # Handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # This block always executes
    print('This is always executed')

# print('The value of a/b is: ')
# assert b != 0, "Divide by 0 error"
# print(a / b)

'''del'''
my_variable1 = 20
my_variable2 = "GeeksForGeeks"

# check if my_variable1 and my_variable2 exists
print(my_variable1)
print(my_variable2)

# delete reference to both variables
del my_variable1
del my_variable2

# check if my_variable1 and my_variable2 exists
# print(my_variable1)
# print(my_variable2)


'''Global and Nonlocal varialbles'''
# global variable
a = 15
b = 10

# function to perform addition
def add():
    c = a + b
    print(c)

# calling a function
add() # Prints 25

# nonlocal keyword
def fun():
    var1 = 10

    def gun():
        # tell python explicitly that it
        # has to access var1 initialized
        # in fun on line 182
        # using the keyword nonlocal
        nonlocal var1

        var1 = var1 + 10
        print(var1)

    gun()

fun() # Prints 20
