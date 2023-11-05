#056
import random

random_number = random.randint(1, 10)

user_input = int(input("Enter a number between 1 and 10: "))

while user_input != random_number:
    user_input = int(input("Try again. Enter a number between 1 and 10: "))

print("Congrats! You guessed the number correctly.")


#057
import random

random_number = random.randint(1, 10)

user_input = int(input("Enter a number between 1 and 10: "))

while user_input != random_number:
    if user_input > random_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    user_input = int(input("Try again. Enter a number between 1 and 10: "))

print("Congrats! You guessed the number correctly.")


