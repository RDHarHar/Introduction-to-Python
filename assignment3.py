# 1. Ryan Harwick
# 2. 2022-02-16
# 3. Assignment 3

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']


def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

### You Code Here

# For testing

print(colors)

guessChance = [1, 2, 3, 4, 5]
ansList = ""


print("Welcome to Mastermind!")
print("Possible colors are: R, G, B, Y, W, O, M, and V")
print("Please enter your guess with no spaces between colors. Colors cannot be repeated\n")

for currentGuess in guessChance:

    if ansList == "RRRR":
        print("Congratulations, you win!")
        break
    else:
        userGuess = input(f"Guess {currentGuess}: ")
        userGuess = userGuess.upper()
        ansList = ""
        invalid = 0

        for l in range(len(userGuess)):
            if userGuess[l] not in legal_colors:
                print(f"Invalid Input: {userGuess[l]} is not a valid color, try again.")
                invalid = 1
                break

        if invalid == 0:
            for j in range(len(userGuess)):
                if j < 3:
                    if userGuess[j] == userGuess[j+1]:
                        print("Invalid input: Colors cannot be duplicated")
                    elif userGuess[j] == colors[j]:
                        ansList = ansList + 'R'
                    elif userGuess[j] in colors:
                        ansList = ansList + 'W'
                    else:
                        ansList = ansList + '_'
                else:
                    if userGuess[j] == colors[j]:
                        ansList = ansList + 'R'
                    elif userGuess[j] in colors:
                        ansList = ansList + 'W'
                    else:
                        ansList = ansList + '_'
            print(ansList)

        if currentGuess == 5 and ansList != "RRRR":
            print("You lose.")
