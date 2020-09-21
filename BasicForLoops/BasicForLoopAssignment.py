"""
Author: Elijah Morishita
elmorishita@dmacc.edu
9/21/2020
This is a basic for loop program that displays the results of two
basic for loops, one iterating thorugh a list of floating point
numbers, the other iterating from 99 - 33 by 2's (odd #'s)
"""

floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1]

for i in range(0, 10):
    print(floats[i]) #  This prints out the contents of 'floats'

print('\n') #  Just a space

x = 99
for x in range(99, 32, -2):
	print(x) #  This prints 99 - 33 by 2's backwards
