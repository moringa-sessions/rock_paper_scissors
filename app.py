import random
choices= ["rock", "paper", "scissors"]
random.shuffle(choices)
computer_choice = choices[0]
print(computer_choice)


def game(user_choice):
    if user_choice=="rock" and computer_choice=="rock":
        print("It's a Tie")

    elif user_choice=="paper" and computer_choice=="paper":
        print("It's a Tie")

    elif user_choice=="scissors" and computer_choice=="scissors":
        print("It's a Tie")
    
    # same
    elif user_choice=="rock" and computer_choice=="scissors":
        print("You won!")

    elif user_choice=="scissor" and computer_choice=="rock":
        print("You Loose!")
    
    # same
    elif user_choice=="rock" and computer_choice=="paper":
        print("You Loose!")

    elif user_choice=="paper" and computer_choice=="rock":
        print("You won!")
    
    # same
    elif user_choice=="scissors" and computer_choice=="paper":
        print("You won!")

    elif user_choice=="paper" and computer_choice=="scissors":
        print("You Loose!")

game("rock")
