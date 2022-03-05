from functions import dict_create, random_word, blank, hangman_game

words = dict_create()
while True:
    word = random_word(words)
    disp = blank(word)

    hangman_game(word, disp)
    check = input("Do You want to play again? (Y)es/(N)o").lower()
    if check == "n":
        print("Exiting the game")
        break
