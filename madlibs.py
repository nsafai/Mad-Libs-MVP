import random
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
                print("\n\n\n")
                print("Build a %s" % listOfThings[random.randrange(0,(len(listOfThings)-1),1)])
                print("Inspired by %s" % listOfCompanies[random.randrange(0,(len(listOfCompanies)-1),1)])
                print("That is %s" % listOfAdjectives[random.randrange(0,(len(listOfAdjectives)-1),1)])
                print("Through %s" % listOfTechnologies[random.randrange(0,(len(listOfTechnologies)-1),1)])
                print("Using %s" % listOfTechniques[random.randrange(0,(len(listOfTechniques)-1),1)])
                userWantsNewStory = False
            if userWantsNewStory == False:
                satisfied = input("\n\n Are you pleased with your story? Type (yes/no): ")
                if satisfied == "yes":
                    print("Goodbye!")
                    running = False
                elif satisfied == "no":
                    print("Ok, here's another one:\n\n")
                    userWantsNewStory = True

    # (1) take input from user

    elif activeList == listOfThings:
        if instructionsNeeded == True:
            user_input(line + "Name a THING and press enter. Then name another. When you're done naming things, type 'done'" + line)
            instructionsNeeded = False
        else:
            user_input('')

    elif activeList == listOfCompanies:
        if instructionsNeeded == True:
            user_input(line + "Name a COMPANY / STORY and press enter. Then name another. When you're done naming companies, type 'done'" + line)
            instructionsNeeded = False
        else:
            user_input('')

    elif activeList == listOfAdjectives:
        if instructionsNeeded == True:
            user_input(line + "Name an ADJECTIVE and press enter. Then name another. When you're done naming adjectives, type 'done'" + line)
            instructionsNeeded = False
        else:
            user_input('')

    elif activeList == listOfTechnologies:
        if instructionsNeeded == True:
            user_input(line + "Name a TECHNOLOGY / PROCESS and press enter. Then name another. When you're done naming technologies, type 'done'" + line)
            instructionsNeeded = False
        else:
            user_input('')

    elif activeList == listOfTechniques:
        if instructionsNeeded == True:
            user_input(line + "Name a TECHNIQUE / INGREDIENT and press enter. Then name another. When you're done naming techniques, type 'done'" + line)
            instructionsNeeded = False
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
