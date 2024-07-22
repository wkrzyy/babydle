# importing modules
import csv
import random


 
# open the file in read mode - That's what the 'r' means
filename = open('baby-names-4.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
names = []

# Assuming the column name is "names"
for row in file:
    names.append(row['name'])


# printing lists
print(len(names))
print('Names:', names)

def setUpGame():
    answer = names[random.randint(0, len(names))]
    answer = answer.lower()
    #print(answer)

    numberOfGuesses = 0
    gameWon = False


def playGame():
    #Game Loop/Update Loop
    while(1):
        #guess: Stores the users Guess
        guess = input("Make a guess: ")
        guess = guess.lower()
        #temp: Tracks which letters in guess are in the correct location, wrong location, and misplaced location.
        # "✓" = the letter is in the correct location
        # "X" = the letter is in the wrong location
        # "-" = the letter is in a misplaced location
        # "?" = the letter could be misplaced or in the wrong location
        temp = ""
    
        if(len(guess) != len(answer)):
            print("Only use " + str(len(answer)) + " characters.")
        elif(guess == answer):
            print("You are correct! The name was " + answer)
            print("It took you " + str(numberOfGuesses) + " guesses")
            print("")
            print("")
            print("A new Game Has Started")
        
            answer = names[random.randint(0, len(names))]
            answer = answer.lower()
            #print(answer)
            numberOfGuesses = 0
            gameWon = False
        else:
            for i in range(0, len(guess)):
                if(guess[i] == answer[i]):
                    temp += "✓"
                elif(guess[i] != answer[i] and guess[i] not in answer):
                    temp += "X"
                else:
                    temp += "-"
        print(temp)
        numberOfGuesses += 1

def main():
    setUpGame()
    playGame()

main()
