import random
from hangman_art import stages, hangman
from hangman_words import word_list

def display_main_logo():
    """Display the Hangman game logo."""
    print(hangman)

def initialize_game(word):
    """Initialize game state with lives and placeholder for the word."""
    lives = 6
    placeholder = " _" * len(word)
    return lives, placeholder

def select_word(word_list, difficulty=2):
    """Select a random word based on difficulty level."""
    if difficulty == 1:  # Easy
        secret_word = random.choice(word_list["easy"])
    elif difficulty == 2:  # Medium
        secret_word = random.choice(word_list["medium"])
    else:  # Hard
        secret_word = random.choice(word_list["hard"])
    return secret_word

def display_stage(lives):
    """Display the current hangman stage based on lives remaining."""
    print(stages[lives])

def check_game_over(lives, word, display):
    """Check if the game is over (win or lose)."""
    if lives == 0:
        return True, False  # Game over, player loses
    if "_" not in display:
        return True, True   # Game over, player wins
    return False, False     # Game continues

def result(won, word):
    """Display the game result."""
    if won:
        print("*************************YOU WIN!***************************")
    else:
        print(f"THE CORRECT WORD WAS {word.upper()}! YOU LOSE!")
        print("*****************************YOU LOSE!****************************")

def play():
    """Run the Hangman game with an option to play again."""
    while True:
        display_main_logo()
        
        # Select difficulty (default to medium for this example; could be user input)
        difficulty = 2  # Can be modified to accept user input (1, 2, or 3)
        secret_word = select_word(word_list, difficulty)
        
        # Initialize game state
        lives, placeholder = initialize_game(secret_word)
        print(f"Word to guess: {placeholder}")
        
        correct_letters = []
        game_over = False
        
        while not game_over:
            print("Guess a letter:")
            guess = input().lower()
            
            # Check for repeated guesses
            if guess in correct_letters:
                print(f"You've already guessed {guess}, try another letter.")
                display_stage(lives)
                continue
            
            # Build display string
            display = ""
            for letter in secret_word:
                if guess == letter:
                    display += guess
                    correct_letters.append(guess)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"
            print(display)
            
            # for incorrect guess
            if guess not in secret_word:
                lives -= 1
                print(f"You've guessed {guess}, that's not in the word; you lose a life.")
                print(f"**********YOU'VE GOT {lives}/6 LIVES LEFT!***********")
            
            # Display current stage
            display_stage(lives)
            
            # Check game status
            game_over, won = check_game_over(lives, secret_word, display)
            
            # Display result if game is over
            if game_over:
                result(won, secret_word)
        
        # Prompt to play again
        print("Would you like to play again? yes / no: ", end="")
        play_again = input().lower()

        
        if play_again == "no":
            print("Thank you for playing Hangman!")
            break
        elif play_again == "yes":
            continue
            print("Starting a new game...")

# Start the game
if __name__ == "__main__":
    play()