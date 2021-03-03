""" A game to guess a number that user entered between 1 and 50 in 10 guesses """

import random 

name = input("What's your name?\n ")
print("hey " + name.title() + "guess a number between 1 and 100 in 10 guesses!")

guess_taken = 0

answer = random.randint(1,100)
print("Make a guess " + name.title())
while guess_taken < 10:
    user_guess = input()
    guess = int(user_guess)
    guess_taken += 1
    if guess < answer:
        print("Guess higher")
    elif guess > answer:
        print("guess lower")
    elif guess == answer:
        break  
print("game over\n")
print("You took " + str(guess_taken) + " guesses")

