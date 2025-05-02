import random
from hangman_art import stages, hangman
from hangman_words import word_list

print(hangman)
random_choice = random.choice(word_list)
# print(random_choice)

### hey its me pratham contriting this code
### i am trying to add some more features to this game

lives = 6

placeholder = ""
for char in range(0, len(random_choice)):  
    placeholder = placeholder + " _"
print(f"Word to guess: {placeholder}")

correct_word = []
   
game_over = False
while not game_over:
    guess = input("Guess a letter:\n").lower()

    if guess in correct_word:
        print(f"You've already guessed {guess}, try another word.")

    display = ""
    for letter in random_choice:
        if guess == letter:
            display += guess
            correct_word.append(guess)
        elif letter in correct_word:
            display += letter 
        else:
            display += "_"
    print(display)

    

    if guess not in random_choice:
            lives = lives - 1
            print(f"You've guessed {guess}, that's not in the word; you lose a life.")
            print(f"**********YOU'VE GOT {lives}/6 LIVES LEFT!***********")
            if lives == 0:
                game_over = True
                print(f"THE CORRECT WORD WAS {(random_choice).upper()}! YOU LOSE! ")
                print("*****************************YOU LOSE!****************************")

    if "_" not in display:
        game_over = True
        print("*************************YOU WIN!***************************")

    print(stages[lives])     