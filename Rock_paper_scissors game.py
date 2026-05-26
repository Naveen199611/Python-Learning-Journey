import random
options=["rock","paper","scissors"]
user_score=0
computer_score=0
while True:
    user_input=input("select any one of rock, paper, scissors: ")
    if user_input not in options:
        print("Invalid input")
        continue
    computer=random.choice(options)
    print(f"You selected: {user_input}")
    print(f"computer selected: {computer}")
    if user_input==computer:
        print("----------------------------------")
        print("It's tie")
        print("----------------------------------")
    elif ((user_input=="rock" and computer=="scissors") or 
        (user_input=="paper" and computer=="rock") or 
        (user_input=="scissors" and computer=="paper")):
        print("----------------------------------")
        print("You Win!")
        print("----------------------------------")
        user_score+=1
    else:
        print("You Lost, Better Luck Next Time!")
        computer_score+=1
    print("----------------------------------")
    print(f"User Score is: {user_score}")
    print(f"Computer Score is:{computer_score}")
    print("----------------------------------")
    play_again= input("Do you want to play again, yes/no: ").lower()
    if play_again!="yes":
        break
print("----------------------------------")
print(f"User Final Score is {user_score}")
print(f"Computer Final Score is {computer_score}")
print("----------------------------------")
print("Thanks for Playing")