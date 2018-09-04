line = "\n_______________________________________________________________________________________________\n"
instructionsNeeded = True
userWantsNewStory = True

listOfThings = list()
listOfCompanies = list()
listOfAdjectives = list()
listOfTechnologies = list()
listOfTechniques = list()

lists = [listOfThings, listOfCompanies, listOfAdjectives, listOfTechnologies, listOfTechniques]

listIndex = 0

numberOfLists = len(lists)

def create(item):
    activeList.append(item)
    # print(', '.join(activeList))

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    create(user_input)

running = True
while running:
    activeList = lists[listIndex]

    if (len(activeList)!=0) and (activeList[-1] == "done"):
        # go to next list
        if listIndex != (numberOfLists-1):
            instructionsNeeded = True
            listIndex = listIndex + 1

        # user is done with lists, show story
        else:
            if userWantsNewStory == True:
                print("Build a %s" % listOfThings[0])
                print("Inspired by %s" % listOfCompanies[0])
                print("That is %s" % listOfAdjectives[0])
                print("Through %s" % listOfTechnologies[0])
                print("Using %s" % listOfTechniques[0])
                userWantsNewStory = False
            if userWantsNewStory == False:
                satisfied = input("\n\n Are you pleased with your story? Type (yes/no): ")
                if satisfied == "yes":
                    print("Goodbye!")
                    running = False
                elif satisfied == "no":
                    print("Ok, here's another one:\n\n")
                    userWantsNewStory == True

    # (1) take input from user

    elif activeList == listOfThings:
        if instructionsNeeded == True:
            user_input(line + "Name a thing and press enter. Then name another. When you're done naming things, type 'done'" + line)
            instructionsNeeded = False
        else:
            user_input('')

    elif activeList == listOfCompanies:
        if instructionsNeeded == True:
            user_input(line + "Name a company and press enter. Then name another. When you're done naming companies, type 'done'" + line)
        else:
            user_input('')

    elif activeList == listOfAdjectives:
        if instructionsNeeded == True:
            user_input(line + "Name an adjective and press enter. Then name another. When you're done naming adjectives, type 'done'" + line)
        else:
            user_input('')

    elif activeList == listOfTechnologies:
        if instructionsNeeded == True:
            user_input(line + "Name a technology and press enter. Then name another. When you're done naming technologies, type 'done'" + line)
        else:
            user_input('')

    elif activeList == listOfTechniques:
        if instructionsNeeded == True:
            user_input(line + "Name a technique and press enter. Then name another. When you're done naming techniques, type 'done'" + line)
        else:
            user_input('')

    else:
        # catch all
        print("unexpected edge case")


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
