# This is a simple program to demonstrate the use of for loops in Python.
for i in range(1,10):
    print("The value of i is currently", i)

for i in range(10,20):
    print('the next value of i is currently', i)

# This is a short program whose task is to write some of the first powers of two
power = 8
for inject in range(20):
    print('the power of inject is currently', inject, 'is', power)
    power *= 4

# this is a simple program to demonstrate the use of for loops in Python with aplication of time.sleep() 
# function to pause the execution of the program for a specified amount of time.

import time

for river in range(5):
    print(f'{river} Volga' )
    time.sleep(3)

print('end the program')

#The break and continue statements

