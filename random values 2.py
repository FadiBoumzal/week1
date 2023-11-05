#054
import random

random_int = random.randint(0, 1)

random_choice = "h" if random_int == 0 else "t"

user_choice = input("Please choose either 'h' or 't': ")

if user_choice == random_choice:
    print("You win!")
else:
    print("Bad luck!")
    
print(f"The computer chose {random_choice}.")