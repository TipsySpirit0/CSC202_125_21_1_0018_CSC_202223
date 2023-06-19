import random

print("Welcome to my number guessing game: ")
print("Im thinking of a number between 1 and 100")

# Pick a random number
number = random.randint(1, 100)
print(number)

# Difficulty

guesses = 0

difficulty = input("Choose a Difficulty, 'easy' or 'hard': ").lower()
playing = True

if difficulty == 'easy':
    guesses = 10
    print(f"You have {guesses} attempts to guess the number")
elif difficulty == 'hard':
    guesses = 5
    print(f"You have {guesses} attempts to guess the number")
else:
        print("Enter a valid choice")

while playing:

    # guessing
    choice = int(input("Guess a number: "))


    if choice == number:
        print("You Guessed The Correct Number🎉🎉")
        playing = False

    # Accuracy
    elif choice > number:
        print("Too high")
        guesses -= 1
        print(f"you have {guesses} left")
    
    elif choice < number:
        print("Too low")
        guesses -= 1
        print(f"you have {guesses} left")

    if guesses == 0:
        print("You lose")
        playing = False

        