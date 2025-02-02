#we have to guess the number like within 10 numbers
import random
def guess():
    num = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number (1-10): "))
        if guess < num:
            print("Low!")
        elif guess > num:
            print("High!")
        else:
            print("You guessed it!")
            break

guess()