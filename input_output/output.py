import time

print('test', 'test', sep='-')
print()
print('test2')

'''time module like setTimeOut'''

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Let\'s Go')

# Because of buffering the above code waits 3 seconds but then prints each iteration immediately
# Adding flush can fix that behavior
# Below the code waits 3 seconds between iterations

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush=True)
        time.sleep(3)
    else:
        print('Let\'s GO!!!')

'''Additional Examples'''
# Python 3.x program showing
# how to print data on
# a screen

# One object is passed
print("GeeksForGeeks")

x = 5
# Two objects are passed
print("x =", x)

# code for disabling the softspace feature
print('G', 'F', 'G', sep='')

# using end argument
print("Python", end='@')
print("GeeksforGeeks")


'''IMPORTANT - Print list without for loop'''
# Print without newline in Python 3.x without using for loop

l = [1, 2, 3, 4, 5, 6]

# using * symbol prints the list
# elements in a single line
print(*l)

