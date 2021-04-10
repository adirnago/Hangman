import LogicFunctions

def main():
    """The main of the project
    call to the start, manage and the end of the game"""
    secret_word = LogicFunctions.start_game()
    is_win = LogicFunctions.manage_game(secret_word, [])
    LogicFunctions.end_game(is_win, secret_word)


if __name__ == "__main__":
    main()
