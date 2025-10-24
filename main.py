import random

def choose_letter(guessed_letters):
    # This function collects and validates a single alphabetical character from the user

    valid_letter = False
    while not valid_letter:
        valid_letter = True

        letter_choice = input("Guess a letter")

        # Check that the input is an alphabetical character
        if not letter_choice.isalpha():
            print("Please type a letter of the alphabet")
            valid_letter = False
        # Check that the input is a single character
        elif len(letter_choice) > 1 or len(letter_choice) == 0:
            print("Please type only a single character")
            valid_letter = False
        # Check that the chosen character doesn't already exist in the list of guessed characters
        elif letter_choice.lower() in guessed_letters:
            print("You've already guessed this letter, please type a different one")
            valid_letter = False
        # If letter chosen is valid, return the letter
        else:
            letter_choice = letter_choice.lower()
            return letter_choice

def choose_move():
    # This function will collect and validate the choice of moves from the user, and return the choice if it is valid

    # The only valid moves are the strings "letter" and "word"
    valid_move = False
    while not valid_move:
        valid_move = True
        move_choice = input("Would you like to guess a letter, or guess the word?")

        if move_choice.lower() != "letter" and move_choice != "word":
            print("Please select a valid option: letter or word")
            valid_move = False
        else:
            return move_choice.lower()

def display_board(mistakes, current_guess, guessed_letters):
    # This procedure will display the game information to the user in a visually appealing and informative way

    # Output round title statement
    print()
    print("#------------------New Round------------------#")

    # Output the letters that the user has guessed so far
    print("Letters guessed:", guessed_letters)

    snowman = [
        "    ___    ",
        " __|___|__ ",
        "   ('v')   ",
        "  (  o  )  ",
        "_(   o   )_"
    ]

    # Output a number of rows of the snowman relating to how many mistakes the user has made
    for row in range(mistakes):
        print(snowman[row])

    # Output how many lives the user has
    print("You have", 5-mistakes, "lives left")

    # Output what the current guess is for the user
    print("Current guess:", current_guess)


def choose_random_word():
    # This function will select a random word from a list of words that the user has to guess
    possible_words = [
        "computer",
        "ferrari",
        "processor",
        "bicycle",
        "harmonious"
    ]

    # Select a random number from the available words
    random_number = random.randint(0, len(possible_words) - 1)

    # Make the word be the word at the randomly generated index
    chosen_word = possible_words[random_number]

    return chosen_word

def play_game():
    # This procedure runs the game of snowman. The initial state of the game is set up, and then rounds are repeatedly
     # run until the user guesses the word, or makes 6 mistakes

    # Initialise the start of the game
    mistakes = 0
    word_to_guess = choose_random_word()
    current_guess = ""
    guessed_letters = []

    # Current guess is the same number of "_" as there are letters in the word_to_guess
    for letter in word_to_guess:
        current_guess += "_"

    # The game runs while the word hasn't been guessed, and they've made less than 6 mistakes
    guessed = False
    while not guessed and mistakes < 6:
        input("Press enter to continue")
        display_board(mistakes, current_guess, guessed_letters)

        # Player selects their move
        move_choice = choose_move()

        # If the move is to select a letter, collect a letter from the user and act appropriately
        if move_choice == "letter":
            letter_choice = choose_letter(guessed_letters)
            guessed_letters.append(letter_choice)

            # If the letter exists in the word_to_guess, update the current guess
            if letter_choice in word_to_guess:
                print("You've guessed a correct letter!")

                new_guess = ""
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == letter_choice:
                        new_guess += letter_choice
                    else:
                        new_guess += current_guess[i]

                current_guess = new_guess

                # If the player has guessed every letter in the word, they win
                if current_guess == word_to_guess:
                    print("You've guessed all the letters!")
                    guessed = True
            # If the letter doesn't exist in the word_to_guess, increment the mistakes
            else:
                print("You haven't guessed a correct letter")
                mistakes += 1
        # If the move is to guess a word, collect the word and act appropriately
        else:
            word_choice = input("What do you think the word is?")

            # If the word guessed is the same as the word_to_guess, the user has won!
            if word_choice.lower() == word_to_guess:
                print("You've correctly guessed the word!")
                guessed = True
            # If the word guessed is not the same as the word_to_guess, increment the mistakes
            else:
                print("That isn't correct...")
                mistakes += 1

    # If, once the game ends, the word hasn't been guessed, the player must have run out of lives. Output a statement
     # letting them know this is the case
    if not guessed:
        print("Unfortunately, you've run out of lives. You lose!")


play_game()