## The program Generates a random number, and the user guesses it with hints provided
import random

# generating random number between 1 to 1000
rand_num = random.randint(1, 1000)
user_input = int(input("Enter any number between 1 and 1000:"))

def guess(rand_num, user_input):
    if  rand_num == user_input:
        print("right guess")
    else:
        print(f"Wrong guess. the right number was:: {rand_num}")

guess(rand_num,user_input)
