answer = "test"
print(answer[0])

while(1):
    guess = input("Make a guess: ")
    #guess = list(guess)
    #answer = list(answer)
    temp = ""
    for i in range(0, len(guess)):
        if(guess[i] == answer[i]):
            temp += "✓"
        elif(guess[i] != answer[i] and guess[i] not in answer):
            temp += "X"
        else:
            temp += "-"
        print(temp)

