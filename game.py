



from random import choice

valid_choices = ["rock", "paper", "scissors"]


def winner(user_choice, computer_choice):
    if user_choice == "rock" and computer_choice == "rock":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        #print("The user wins")
        return "The user wins"

    elif user_choice == "paper" and computer_choice == "rock":
        #print("The computer wins")
        #return "The computer wins"
        return "The user wins"
    elif user_choice == "paper" and computer_choice == "paper":
        #print("It's a tie!")
        return "It's a tie!"
    elif user_choice == "paper" and computer_choice == "scissors":
        #print("The user wins")
        #return "The user wins"
        return "The computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        #print("The computer wins")
        return "The computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        #print("The user wins")
        return "The user wins"
    elif user_choice == "scissors" and computer_choice == "scissors":
        #print("It's a tie!")
        return "It's a tie!"


if __name__ == "__main__":

    # ONLY RUN THE FOLLOWING CODE IF RUN THIS SCRIPT FROM COMMAND LINE


    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_choices)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    # USE THE FUNCTION FROM ABOVE????

    print(winner(u, c))
