import random

line = "\n_______________________________________________________________________________________________\n"
instructionsNeeded = True
userWantsNewStory = True

listOfProducts = list()
listOfCompanies = list()
listOfAdjectives = list()
listOfTechnologies = list()
listOfTechniques = list()

arrayOflists = [listOProducts, listOfCompanies, listOfAdjectives, listOfTechnologies, listOfTechniques]
numberOfLists = len(arrayOflists)
listIndex = 0

def create(item):
    # if input is not empty
    if item != "":
        # add input to list
        activeList.append(item)

running = True
while running:
    activeList = arrayOflists[listIndex]

    # if list is not empty and last item of list is not "done"
    if (len(activeList)!=0) and (activeList[-1] == "done"):
        # if you're not on the last list
        if listIndex != (numberOfLists-1):
            instructionsNeeded = True
            listIndex = listIndex + 1

        # user is done with lists, show story
        else:
            if userWantsNewStory == True:
                print("\n\nYour inspiration:\n")
                # random.randrange (startpoint, endpoint, increment-interval)
                print("Build a %s" % listOfProducts[random.randrange(0,(len(listOfProducts)-1),1)])
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
    elif activeList == listOfProducts:
        if instructionsNeeded:
            create(str(input(line + "Name a TYPE OF PRODUCT and press enter. Then name another. When you're done, type 'done'" + line)))
            instructionsNeeded = False
        else:
            create(input(''))

    elif activeList == listOfCompanies:
        if instructionsNeeded:
            create(str(input(line + "Name a COMPANY / STORY and press enter. Then name another. When you're done, type 'done'" + line)))
            instructionsNeeded = False
        else:
            create(input(''))

    elif activeList == listOfAdjectives:
        if instructionsNeeded:
            create(str(input(line + "Name an ADJECTIVE and press enter. Then name another. When you're done, type 'done'" + line)))
            instructionsNeeded = False
        else:
            create(input(''))

    elif activeList == listOfTechnologies:
        if instructionsNeeded:
            create(str(input(line + "Name a TECHNOLOGY / PROCESS and press enter. Then name another. When you're done, type 'done'" + line)))
            instructionsNeeded = False
        else:
            create(input(''))

    elif activeList == listOfTechniques:
        if instructionsNeeded:
            create(str(input(line + "Name a TECHNIQUE / INGREDIENT and press enter. Then name another. When you're done, type 'done'" + line)))
            instructionsNeeded = False
        else:
            create(input(''))

    else:
        # catch all
        print("Something's wrong")
