# Guess the Number
# There's a secret number between 1 and 20. You have 6 tries to guess right or you lose!
import random

# Store number of guess in the variable. Starts off with 0 because player hasn't made any guesses yet.
guessesTaken = 0

# Establish the start of game play with basic print function.
# Create variable so that the user can interact with the program via their own input
print('Hello! What is your name?')
myName = input()

# Call randint function and store value in number
# Randint is established when we imported random
# Random.randint tells the program that it is from the import
# Concatenate 3 strings into one print statement
number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 an 20.')

# Establishing first for loop of the game
# This loop will execute 6 times or less depending on the guess
# A for statement always has a colon after the condition
# After for statement, establish new variable name
# The in calls the range function and establishes how many times it will loop
# Each time the execution goes through the loop, it is called an iteration
for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    # To pass a string to an integer the string must be a number
    guess = int(guess)

    # Establishing Boolean data types that will result in either True or False
    # Conditions are expressions that use comparison operators like < and >
    # If statement will only run if it is True. If it is False, then the block gets skipped
    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Great Job, ' + myName + ' you guessed my number in ' + guessesTaken + ' guesses!');

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
