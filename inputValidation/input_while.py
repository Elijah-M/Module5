"""
Author: Elijah Morishita
elmorishita@dmacc.edu
9/21/2020
This is an input validation while loop program that tests input
gathered from the user between 1 - 100, prompting until it's
in the correct range.
"""

MIN = 1
MAX = 100

user_input = []  # Used to store user input
end_loop = -1  # Used to break the loop (sentinel)
index = 0  # An index for iterating through the for loop

choice = int(input("Please enter a number between 1 - 100, or -1 to quit: "))

while choice != end_loop:
    while choice < MIN or choice > MAX:  # checks if user input is between 1 - 100
        choice = int(input("Invalid input, please enter a number between 1 - 100: "))

    user_input.append(choice)  # add user input to a list
    choice = int(input("Please enter a number between 1 - 100, or -1 to quit: "))
    index = index + MIN  # adding to the iterator for the for loop

print("\n============================================\n", "Results:\n")  # a divider for spacing

for i in range(0, index):
    print(user_input[i])  # prints only valid entries from the user_input list

"""
Observed output:
Numeric input seems to work well as long as the user enters whole numbers, if the user enters
a float or alpha character the program will crash - ValueError
"""