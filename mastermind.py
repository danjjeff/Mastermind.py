# I'm (a) coding Mastermind here!
# Written by Danny Brown on November 19, 2017
import random, re, sys

if sys.version_info[0] < 3:
        raise "Must be using Python 3"

# Function Definitions
def validateDifficulty():
    while True:
        try:
            newDiff = int(input("Select a difficulty between 2 and 9: "))
        except ValueError:
            print("That's not a valid value. ", end='')
            continue
        if newDiff > 9 or newDiff < 2:
            print("That's not a valid value. ", end='')
            continue
        else:
            return newDiff   

def generateBoard(difficulty):
    newBoard = []
    for x in range(4):
        newBoard.append(random.randint(1, difficulty))
    return newBoard

def guessFunc(diff):
    guess = str(input(": ")) # accepts guess in format like '1234'
    while not re.match("[1-" + str(diff) + "][1-" + str(diff) + "][1-" + str(diff) + "][1-" \
                       + str(diff) + "]", guess) or len(guess) != 4: # validates guess
        guess = str(input("No. Guess exactly four numerals between 1 and " + str(diff) +":\n > "))
    guessList = list(guess) # turn guess into a list of characters like ['1', '2', '3', '4']
    guessList = list(map(int, guessList)) # turn lists of chars into list of ints like [1, 2, 3, 4]
    return guessList 

def compareLists(list1, list2):
    matchCount = 0
    for index in range(4):
        if list2[index] == list1[index]:
            matchCount += 1
            print(" *", end='')
    if matchCount == 4:
        print("\n\nYou win!")
        print("The board was: ", end='')
        print(board)
        return True
    else:
        print()
        return False        

# Main
difficulty = validateDifficulty()
board = generateBoard(difficulty)

print("\n*********************************INSTRUCTIONS*********************************")
print("You are guessing four numbers in a particular order ranging from 1 to " + str(difficulty) + ".")
print("The * symbols indicate how many of your numbers are correct, but not which.")
print("You will have 10 guesses before you are a loser. Guess right to be a winner!")
print("Format your guesses like this: 1234, 1414, 1111, etc. Duplicates are possible.")
print("******************************************************************************\n")

guessCount = 0
winner = False

while winner == False:
    guessCount += 1
    if guessCount > 10:
        print("You lose!")
        print("The board was: ", end='')
        print(board)
        break
    print("Guess #" + str(guessCount), end='')
    guessList = guessFunc(difficulty)
    winner = compareLists(board, guessList)    
