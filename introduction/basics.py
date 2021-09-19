'''List'''
# Creates an empty list
nums = []
# Appending data to list
nums.append(21)
nums.append('40.7')
nums.append('Derrick')
print(nums)

'''Input'''
# Getting input from user
name = input("Enter your name: ")
print('Hello', name)

# Calculate sum from input
num1 = int(input('Enter Number: '))
num2 = int(input('Enter Number: '))
sum = num1 + num2
print(num1,  '+', num2, '=', sum)

'''Selection'''
num1 = 34
if(num1 < 12):
    print('Num1 is less than 12')
elif(num1 < 35):
    print('Num1 is greater than 12 but less than 35')
else:
    print('Num1 is', num1)

'''Function'''
def hello(name = 'Derrick'):
    print('Hello', name)
# Call function
hello()
hello('Sam')

'''Iteration'''
# for Loop
for step in range(8):
    print(step)

'''Modules'''
import math
def Main():
    num = -85
    # fabs gives you the absolute value of a decimal
    num = math.fabs(num)
    print('Abs:', num)
# Call function
if __name__ == "__main__":
    Main()