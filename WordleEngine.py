# importing modules
import csv
import random

def main(): 
    # open the file in read mode - That's what the 'r' means
    filename = open('baby-names-4.csv', 'r')
 
    # creating dictreader object
    file = csv.DictReader(filename)
 
    # creating empty lists
    names = []

    # Assuming the column name is "names"
    for row in file:
        names.append(row['name'])
    #print("DEBUG" + len(names))
    #print("DEBUG: " + 'Names:', names)

    answer = names[random.randint(0, len(names))]
    answer = answer.lower()
    
    #Game Loop/Update Loop
    numberOfGuesses = 0
    #print("DEBUG: " + answer)
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
        temp2 = answer
    
        if(len(guess) != len(answer)):
            print("Only use " + str(len(answer)) + " characters.")
        elif(guess == answer):
            print("You are correct! The name was " + answer)
            print("It took you " + str(numberOfGuesses + 1) + " guesses")
            print("")
            print("")
            print("A new Game Has Started")
        
            answer = names[random.randint(0, len(names))]
            answer = answer.lower()
            #print("DEBUG: " + answer)
            numberOfGuesses = 0
        else:
            for index in range(0, len(guess)):
                if(guess[index] == temp2[index]):
                    temp += "✓"
                    temp2 = temp2.replace(guess[index], "^",1)
                else:
                    temp += "?"
            for index in range(0, len(guess)):
                if(guess[index] != temp2[index] and temp[index] == "?" and guess[index] not in temp2):
                    temp = temp[:index] + "X" + temp[index + 1:]
                elif(temp[index] == "?"):
                    temp = temp[:index] + "-" + temp[index + 1:]
                    temp2 = temp2.replace(guess[index], "^",1)
            numberOfGuesses += 1
        print(temp)

main()
