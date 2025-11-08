#James Van Dyk
#4.1
#number guessing game

from random import randint

secret = randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("Just right!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")