
#To generate a random number, I am importing a python module called random.
import random

#Now I'm setting my number variable and using the random module to generate a number between 1-10 and store in that variable.
number = random.randint(1, 10)

#Now I'm using raw_input to ask the user their name.
raw_input("Drop your nickname")

#And I want to saw that raw input into a variable which will store it.
userName = raw_input

print("Whats up " + userName)

#Now I'm creating this numberOfGuesses variable and assigning 0 to it.
numberOfGuesses = 0

#Now I want to print a string with the user's name in it. 
print('Are you ready? '+ userName+ ' I am guessing a number between 1 and 10')

#Now I'm making my while loop. 
while numberOfGuesses < 5:

    #This guess variable is where the guess numbers will be stored.
    guess = int(input())
    numberOfGuesses += 1
    if guess < number:
        print('You guessed too low!')
    if guess > number:
        print('Try again, your guess is too high!')
    if guess == number:
        break
if guess == number:
    print('You guessed it right ' + str(numberOfGuesses) + 'attempts!')
else:
    print('You got it wrong! It was ' + str(number))
