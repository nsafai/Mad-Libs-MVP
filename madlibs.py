## Product Requirements

# (1) Display story with blanks for input words
#

listOfThings = list()
numberOfThings = 0

def create(item):
    listOfThings.append(item)
    print(listOfThings)
    print(numberOfThings)


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    print(prompt)
    create(user_input)

running = True
while running:
    numberOfThings = numberOfThings + 1

    if numberOfThings == 1:
        user_input("Name a thing\n")

    elif listOfThings[len(listOfThings)-1] == "done":
        running = False

    else:
        user_input("Name another thing. When you're done naming things, type 'done'\n")





# (2) Inputs:
# thing
# Company name or phenomenon
# positive adjective
# process/technology
# technique
#
# (3) Output:
# Build a [thing]
# Inspired by [Company name or phenomenon]
# That is [positive adjective]
# Through [process/technology]
# Using [technique]
#
# (4) Test user input
#
#
# ## Code requirements
#
# Variable assignment
# Function definitions
# Core data types: strings, integers, floats
# Collection types: lists, tuples, dictionary
#
# ## Stretch Goals
# Randomize the words of the same type (ie shuffle the 5 nouns)).
# Use a dictionary to generate the words.
# Use a differnet data structure to store words.
# Build with TDD
# Use the system module (for accessing command-line arguments)
