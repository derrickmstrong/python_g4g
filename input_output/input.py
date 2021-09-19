'''
Taking input in Python
'''
val = input('Enter your value: ')
print(val)
print(type(val))

# raw_input works in python 2.x
# val = raw_input('Enter your name: ')
# print(val)

# Typecasting val by wrapping it in int() to convert it from a string to a integer
val = int(input('Enter a number: '))
print(val)
print(type(val))

# Typecasting val by wrapping it in float() to convert it from a string to a float
val = float(input('Enter a number: '))
print(val)
print(type(val))

'''Multiple Inputs via split()'''
# Python program showing how to
# multiple input using split

# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

# taking two inputs at a time
a, b = input("Enter a two value: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students grades: ", x)
sum = 0
for grade in x:
    print(grade, end=" ")
    print('\r')
    sum += grade
print('Number of students:', len(x))
print('Average:', sum / len(x))


'''Multiple Inputs via list comprehension'''
# Python program showing
# how to take multiple input
# using List comprehension

# taking two input at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three value: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
print()

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x)
