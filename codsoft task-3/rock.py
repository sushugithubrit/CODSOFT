import random

def get_computer_choice():
    """Generate a random choice for the computer: rock, paper, or scissors."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the Rock, Paper, Scissors game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    """Display the user's choice, computer's choice, and the result."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def play_game():
    """Main function to play the game."""
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game!")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        display_result(user_choice, computer_choice, result)
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()

