
#To generate a random number, I am importing a python module called random.
import random

#Next, I'm making a variable that will store the number between 1-10 that the computer will generate.
number = random.randint(1, 10)

#Now I'm creating a userName variable and inside of it is a prompt for the user to give me their name.
userName = input("Drop your nickname")

#Now I'm creating this numberOfGuesses variable and assigning 0 to it.
numberOfGuesses = 0

#Now I want to print a string with the user's name in it. 
print('Are you ready? '+ userName+ ' I am guessing a number between 1 and 10')

#Now I'm making my while loop. 
while numberOfGuesses < 5:

    #This guess variable is where the guess numbers will be stored.
    guess = int(input())
    numberOfGuesses += 1
    if guess < digit:
        print('You guessed too low!')
    if guess > digit:
        print('Try again, your guess is too high!')
    if guess == number:
        break
if guess == number:
    print('You guessed it right ' + str(numberOfGuesses) + 'attempts!')
else:
    print('You got it wrong! It was ' + str(number))
