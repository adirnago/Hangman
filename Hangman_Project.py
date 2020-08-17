import os

def start_game():
    """This function organizes the beginning of the game
    we call ascii_background for printing the first screen & the max tries (6)
     and we get & check the path file & the index from the user"""
    # for the first time that we call the function "show_hidden_word" we don't have any old letters
    empty_list = []

    # call to the ascii background and the max tries
    ascii_background()
    path_to_file = setPathToFile()
    index_from_user = setIndexFromUser()
    print(starting_faze)

    # choose word according to the user
    secret_word = choose_word(path_to_file, index_from_user)
    # print '_' according to the number of the chars of the word
    show_hidden_word(secret_word, empty_list)
    return secret_word


def ascii_background():
    """Print first ascii background + max tries of failure"""
    print(HANGMAN_ASCII_ART, MAX_TRIES)

def setPathToFile():
    """Get path from the user & check if the path exists"""
    path_to_file = str(input("Please enter path to file: "))
    while (not os.path.exists(path_to_file)):
        print("Your path is not exist")
        path_to_file = str(input("Please enter path to file: "))
    return path_to_file


def setIndexFromUser():
    """Get index from the user & check if it is a positive integer number that
     represent a word index. If it's not we try to get another index"""
    is_valid_number = False
    temp_index = (input("Please enter positive integer number that represent a word index: "))

    while (not is_valid_number):
        if (temp_index.isdigit()):
            if (int(temp_index) % 1 != 0) or int(temp_index) <= 0:
                print("Your index must be a positive integer number")
                temp_index = (input("Please enter positive integer number that represent a word index: "))
            else:
                is_valid_number = True
        else:
            temp_index = (input("Your index does not satisfy the policy, Please try another index: "))
    index_from_user = int(temp_index)
    return index_from_user


# this function is choosing a word to guess from a file path that the user gave us
def choose_word(path_to_file, index_from_user):
    """Choosing a word to guess from a file path that the user gave us
    the function got a path_to_file(string) & index_from_user(int)
    and return the word in the index position for the secret word"""
    wordcount = []
    file = open(path_to_file)
    all_word_in_file = file.read().split()

    for word in all_word_in_file:
        if word not in wordcount:
            wordcount.append(word)

    word_location = index_from_user % len(all_word_in_file)
    if word_location == 0:
        word_location += 1
    return all_word_in_file[word_location-1]

    file.close()

def show_hidden_word(secret_word, old_letters_guessed):
    """This function is get a secret_word(string) & old_letter_guessed(list)
    and return the letters from the old_letters_guessed list that are in the secret_word
    string in their respective positions, and the rest of the letters in the string as underscores"""
    for char in secret_word:
        if char in old_letters_guessed:
            print(char, end=' ')
        else:
            print("_", end=' ')
    print("\n")
    return old_letters_guessed

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def manage_game(secret_word, old_letters_guessed):
    """This function is organizes the logic part of the game
     she got a secret_word (string) & old_letter_guessed (list) and check
    if the user success to guess a letter or not and if he is win or lose"""
    num_of_tries = 0

    while (MAX_TRIES > num_of_tries):
        letter_guessed = str(input("Please guess a letter: "))
        if(try_update_letter_guessed(letter_guessed.lower(), old_letters_guessed)):
            old_letters_guessed += [letter_guessed.lower()]
            if letter_guessed.lower() in secret_word:
                show_hidden_word(secret_word, old_letters_guessed)
            else:
                num_of_tries += 1
                print("Bad luck, your guess is not included in the word \n"
                      "Please try another char")
                print(HANGMAN_PHOTOS[num_of_tries])
                show_hidden_word(secret_word, old_letters_guessed)
            if (check_win(secret_word, old_letters_guessed)):
                return True
        #else:
            #print("Your guess is not valid, please try guess again")
        if (num_of_tries > 7):
            print("You lose the game")
    return False

def check_win(secret_word, old_letters_guessed):
    """"This function is got secret_word (string) & old_letters_guessed(list)
     and return if the user is success to guess the all chars or not (boolean)"""
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """"Get true/false from check_valid_input function and if the result is false
     she is printing 'X' & list of your old_letters_guessed
     """
    if not check_valid_input(letter_guessed.lower(), old_letters_guessed):
        print('X')
        print(" -> ".join(old_letters_guessed))
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    """"This function is checked if the letter guessed is one of the abc
     and if she's not guessed before, and return true/false to try_update_letter_guessed function"""
    if (len(letter_guessed.lower()) != 1) \
            or (not letter_guessed.lower().isalpha())\
            or (letter_guessed.lower() in old_letters_guessed):
        return False
    return True


#------------------------------------------------------------------------------------------------------------------------------------------------------------------

def end_game(is_win, secret_word):
    """This function is get result from the manage_game function for win or lose
    and printing a relevant message according to the results"""
    if is_win:
        print("Congratulation, you win the game and the secret word is:", secret_word)
    else:
        print("You failed to guess the secret word \nThe word is:", secret_word)


HANGMAN_ASCII_ART = " _    _\n" \
                    "| |  | |\n" \
                    "| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n" \
                    "|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n" \
                    "| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n" \
                    "|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n" \
                    "                     __/ |                      \n" \
                    "                    |___/                       \n"
MAX_TRIES = 6

starting_faze = ("""
x-------x
""")


HANGMAN_PHOTOS = {1: """
    x-------x
    |
    |
    |
    |
    |
""", 2: """
    x-------x
    |       |
    |       0
    |
    |
    |
""", 3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |       
    |	
""", 5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |	
""", 6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""}


def main():
    """The main of the project
    call to the start, manage and the end of the game"""
    secret_word = start_game()
    is_win = manage_game(secret_word, [])
    end_game(is_win, secret_word)


if __name__ == "__main__":
    main()