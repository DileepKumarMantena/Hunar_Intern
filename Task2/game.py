import random

def get_user_choice():
    choices = ['stone', 'paper', 'scissors']
    user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter stone, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
