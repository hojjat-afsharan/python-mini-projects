#create a random number
#get user input
#compare random number with player input

import random

def play(max):
    random_number = random.randint(1, max)
    number = 0
    counter = 0

    while number != random_number:

        number = int( input(f"Please enter a value between 1 and {max}: "))
        counter += 1

        if number > random_number:
            print("Guess is too high")
        elif number < random_number: 
            print("Guess is too low")
        
    print(f"Yay!! your guess after {counter} guess(es) is correct, the number was {random_number}" )

play(10)