# Hangman. I need to select a word, let the user put in any letter.
# If the letter is in the word then it replaces it.
# Else you get a piece of hangman (lose a choice)
import string
Vword = "Firehose"
alphabets = list(string.ascii_letters)
print(alphabets)
initialList = list(Vword.upper())
word = list(Vword.upper())
output = list('_'*len(word))
userIn = ""
lives = 0
usedL = list()


def hangman():

    if lives == 1:
        print("  |________")
        print("  |       |")
        print("  |    ")
        print("  |   ")
        print("  |  ")
        print("  |   ")
        print("  |   ")
        print("__|__________")
    elif lives == 2:
        print("  |________")
        print("  |      _|_")
        print("  |     {   }")
        print("  |   ")
        print("  |  ")
        print("  |   ")
        print("  |   ")
        print("__|__________")
    elif lives == 3:
        print("  |________")
        print("  |      _|_")
        print("  |     {   }")
        print("  |       |  ")
        print("  |       | ")
        print("  |        ")
        print("  |       ")
        print("__|__________")
    elif lives == 4:
        print("  |________")
        print("  |      _|_")
        print("  |     {   }")
        print("  |       |_  ")
        print("  |       | \ ")
        print("  |    ")
        print("  |      ")
        print("__|__________")
    elif lives == 5:
        print("  |________")
        print("  |      _|_")
        print("  |     {   }")
        print("  |      _|_  ")
        print("  |     / | \ ")
        print("  |         ")
        print("  |          ")
        print("__|__________")
    elif lives == 6:
        print("  |________")
        print("  |      _|_")
        print("  |     {   }")
        print("  |      _|_  ")
        print("  |     / | \ ")
        print("  |      /   ")
        print("  |     /     ")
        print("__|__________")
    elif lives == 7:
        print("  |________")
        print("  |      _|_")
        print("  |     {   }")
        print("  |      _|_  ")
        print("  |     / | \ ")
        print("  |      / \  ")
        print("  |     /   \  ")
        print("__|__________")
    elif lives == 8:
        print("  |________")
        print("  |      _|_")
        print("  |     {;-;}")
        print("  |      _|_  ")
        print("  |     / | \ ")
        print("  |      / \  ")
        print("  |     /   \  ")
        print("__|__________")


while lives < 8:
    print(output)
    print("Lives left: ", 8 - lives)
    userIn = str(input("Enter a letter: "))
    userIn = userIn.upper()
    if userIn not in alphabets:          # checks if it is a letter
        print("Not a letter, try again.")
        continue
    if userIn in output:                # checks used letter in word
        print("Already used")
        continue
    for L in word:
        if userIn == L:
            output[word.index(L)] = L
            word[word.index(L)] = '_'
    if output == initialList:           # checks if wincon reached
        print("You win!")
        print("The word was: ", Vword)
        break
    if userIn not in output:
        if userIn in usedL:             # checks used letter list
            print("Already used")
            continue
        else:                           # if used then goes to used letter list
            usedL.append(userIn)
        lives += 1
        hangman()

else:
    print("You lose")
    print("The word was: ", Vword)
    hangman()


