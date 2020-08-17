#Todo DOCOMANTATION
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

#todo think about singletoon here
# get file path and word index from the user
PATH_TO_FILE = ''
INDEX_FROM_USER = ''

#allowed_char = 'abcdefghijklmnopkrstuvwxyzABCDEFGHIJKLMNOPKRSTUVWXYZ'

HANGMAN_PHOTOS = { 1: """
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
