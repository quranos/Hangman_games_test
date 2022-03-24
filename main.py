import random
# instead of import hangman_word | if u use only 1 function, easy to read code -> when u use val: hangman_word.word_list
from hangman_words import word_list
from hangman_art import logo, stages
# from replit import clear # clear

chosen_word = random.choice(word_list) # random word in list
word_length = len(chosen_word) # count how many letters in word
end_of_game = False # set value for check game end/not
lives = 6 # set live = 6 | if 0 = end

print(logo)
# Create blanks ['_', '_', '_', ...]
display = []
for _ in range(word_length):
    display += "_"
    
print(f"\nPssst, the solution is {''.join(display)}.") # join all elements in the list -> string

# repeat loop if game not end yet
while not end_of_game:
    print("=================================================================\n")
    guess = input("Guess a letter: ").lower() # value user guess letter
    # clear() # clear
    len_guess = len(guess) # Note: check how many user input | !bug!
        
    if guess in display: # if user already guess same letter before let them know
        print(f"You've already guessed '{guess}'")
        
    # check user guess letter
    for position in range(word_length): # loop position till last letter of word
        letter = chosen_word[position] # new value for check every position letter in word
        if letter == guess: # if user letter guess True replace it "_" -> a
            display[position] = letter

    # !!!!! bug just try to limit letter | type > 1 & < 0 !!!!!
    if (len_guess > 1) and (guess in chosen_word):
        print(f"You have to guess ONLY 1 letter. You lose a life.")
        lives -= 1
    elif len_guess == 0:
        print(f"You haven't guess a letter. You lose a life.")
        lives -= 1
    # !!!!! bug just try to limit letter | type > 1 & < 0 !!!!!
        
    # Check if user guess wrong      
    elif guess not in chosen_word: # if user letter != chosen_word | reduce lives 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0: # if lives = 0 | end
            end_of_game = True
            print(f'\nYou lose. (ಥ﹏ಥ) \nThe answer is "{chosen_word}".')

    print(f"{' '.join(display)}")
    
    # Check if user has got all letter | not have any "_"
    if "_" not in display:
        end_of_game = True
        print("\nCongrat!! You win! ღゝ◡╹)ノ♡")

    print(stages[lives])

# NOTE : I try to find the way to limit input str in Python cuz when i type
# eg. word = apple -> I type 'ap' it's correct but code doesn't know which "if" that's to go so none and repeat not even reduce lives
# but if I type 'pa' it's wrong and run to "if guess not in chosen_word:"
# So, I use "if (len_guess > 1) and (guess in chosen_word):" instead || i'm gonna find another way
# and another that i found if I don't type just enter | I use "if len_guess == 0:"