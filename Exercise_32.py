from functions import dict_create, random_word, blank, hangman_game

words = dict_create()
word = random_word(words)
disp = blank(word)

hangman_game(word, disp)
