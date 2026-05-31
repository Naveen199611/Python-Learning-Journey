#Number Guessing Game

import random
guess_number= int(input("guess the number: "))
secret_number=random.randint(1,10)
while guess_number!=secret_number:
    print("Try again")
    print("The Correct number is: ", secret_number)
    guess_number= int(input("guess the number: "))
    secret_number=random.randint(1,10)
else:
    print("Congrats! You guessed it right")
