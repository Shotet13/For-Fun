answer = "_________"
word = "happiness"
correct = ['h','a','p','p','i','n','e','s','s']
incorrect = []
word_length = 9
tries = 0

hangman_stages = [
    " _____\n |/  |\n |   O   \n |       \n |      \n_|_",  # Stage 1
    " _____\n |/  |\n |   O   \n |   |   \n |      \n_|_",  # Stage 2
    " _____\n |/  |\n |   O   \n |  -|   \n |      \n_|_",  # Stage 3
    " _____\n |/  |\n |   O   \n |  -|-  \n |      \n_|_",  # Stage 4
    " _____\n |/  |\n |   O   \n |  -|-  \n |  /   \n_|_",  # Stage 5
    " _____\n |/  |\n |   O   \n |  -|-  \n |  / \ \n_|_"  # Stage 6
]

print(f"You are guessing a {word_length} letter word")

while tries < 6:
    print(f"Current Word: {answer}")
    guess = input("\nEnter your guess: ")
    if guess in correct:
        if guess in answer:
            print("\nYou've already guessed that letter!")
        else:
            print("\nCorrect!")
            for i in range(len(correct)):
                if guess == correct[i]:
                    answer = answer[:i] + guess + answer[i+1:]
    else:
        if guess in incorrect:
            print("\nYou've already guessed that letter!")
        else:
            print("\nIncorrect!")
            incorrect.append(guess)
            print(hangman_stages[tries])
            tries += 1

    if answer == word:
        print(f"\nThe word was: {word}")
        break

else:
    print(f"You died!\nYou got to: {answer}\nThe word was: {word}")

print(f"Incorrect guesses: {incorrect}")