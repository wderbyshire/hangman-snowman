import random

def choose_letter(guessed_letters):
    valid_letter = False
    while not valid_letter:
        valid_letter = True

        letter_choice = input("Guess a letter")

        if not letter_choice.isalpha():
            print("Please type a letter of the alphabet")
            valid_letter = False
        elif len(letter_choice) > 1:
            print("Please type only a single character")
            valid_letter = False
        elif letter_choice.lower() in guessed_letters:
            print("You've already guessed this letter, please type a different one")
            valid_letter = False
        else:
            letter_choice = letter_choice.lower()

    return letter_choice

def choose_move():
    valid_move = False
    while not valid_move:
        valid_move = True
        move_choice = input("Would you like to guess a letter, or guess the word?")

        if move_choice != "letter" and move_choice != "word":
            print("Please select a valid option: letter or word")
            valid_move = False

    return move_choice

def display_board(mistakes, current_guess, guessed_letters):
    print()
    print("#------------------New Round------------------#")
    print("Letters guessed:", guessed_letters)

    snowman = [
        "    ___    ",
        " __|___|__ ",
        "   ('v')   ",
        "  (  o  )  ",
        "_(   o   )_"
    ]
    for row in range(mistakes):
        print(snowman[row])

    print("You have", 5-mistakes, "lives left")

    print("Current guess:", current_guess)


def choose_random_word():
    possible_words = [
        "computer",
        "ferrari",
        "processor",
        "bicycle",
        "harmonious"
    ]

    random_number = random.randint(0, 4)

    chosen_word = possible_words[random_number]

    return chosen_word

def play_game():
    mistakes = 0
    word_to_guess = choose_random_word()
    current_guess = ""
    guessed_letters = []

    for letter in word_to_guess:
        current_guess += "_"

    guessed = False
    while not guessed and mistakes < 6:
        input("Press enter to continue")
        display_board(mistakes, current_guess, guessed_letters)

        move_choice = choose_move()

        if move_choice == "letter":
            letter_choice = choose_letter(guessed_letters)
            guessed_letters.append(letter_choice)

            if letter_choice in word_to_guess:
                print("You've guessed a correct letter!")

                new_guess = ""
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == letter_choice:
                        new_guess += letter_choice
                    else:
                        new_guess += current_guess[i]

                current_guess = new_guess

                if current_guess == word_to_guess:
                    guessed = True
            else:
                print("You haven't guessed a correct letter")
                mistakes += 1
        else:
            word_choice = input("What do you think the word is?")

            if word_choice.lower() == word_to_guess:
                print("You've correctly guessed the word!")
                guessed = True
            else:
                print("That isn't correct...")
                mistakes += 1


    if not guessed:
        print("Unfortunately, you've run out of lives. You lose!")


play_game()