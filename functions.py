import random
import os
import requests


# common numbers function for Exercise_5
def common(a_list, b_list):
    c_list = []
    for a in a_list:
        if a in b_list and a not in c_list:
            c_list.append(a)
    return c_list


# rock, paper, scissors game
def game():
    w_1, w_2 = 0, 0
    player_1 = input("Player One! Choose a answer. Type (R)ock, (P)aper, (S)cissors.")
    player_2 = input("Player Two! Choose a answer. Type (R)ock, (P)aper, (S)cissors.")
    if player_1.lower() == "r" and player_2.lower() == "s":
        print("Player One win!")
        w_1 = 1
        return w_1, w_2
    elif player_1.lower() == "s" and player_2.lower() == "p":
        print("Player One win!")
        w_1 = 1
        return w_1, w_2
    elif player_1.lower() == "p" and player_2.lower() == "r":
        print("Player One win!")
        w_1 = 1
        return w_1, w_2
    elif player_2.lower() == "r" and player_1.lower() == "s":
        print("Player Two win!")
        w_2 = 1
        return w_1, w_2
    elif player_2.lower() == "s" and player_1.lower() == "p":
        print("Player Two win!")
        w_2 = 1
        return w_1, w_2
    elif player_2.lower() == "p" and player_1.lower() == "r":
        print("Player Two win!")
        w_2 = 1
        return w_1, w_2
    else:
        print("It's a tie!")
        w_1 = 1
        w_2 = 1
        return w_1, w_2


# prime number finder
def prime(num):
    list_p = []
    i = 1
    while i <= num:
        if num % i == 0:
            list_p += [i]
        i += 1
    if num == 1:
        print("Number ", num, " is prime!")
    elif len(list_p) == 2:
        print("Number ", num, " is prime!")
    else:
        print("Number ", num, " is not prime...")


# list beginning and ending
def beg_end(a_list):
    new_list = [a_list[0], a_list[len(a_list) - 1]]
    return new_list


# Fibonacci numbers generator
def fibonacci(number):
    num_list = [1, 1]
    if int(number) < 0:
        print("Number must be from 0 to infinity")
    elif int(number) == 0:
        return []
    elif int(number) == 1:
        return [1]
    elif int(number) == 2:
        return num_list
    else:
        for i in range(2, int(number), 1):
            num_list.append(num_list[i-2]+num_list[i-1])
    return num_list


# Removing duplicates - traditional way
def rmv_dup_trad(a_list):
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


# Removing duplicates - with set
def rmv_dup_set(a_list):
    return list(set(a_list))  # without list() it will be the same result but in {} because is it a set not a list


# Exercise_5 in one line
def ex_5_rmv_dup(a_list, b_list):
    return list(set((a_list+b_list)))


# Reversing the string
def rev_str(txt):
    a = txt.split()
    rev_txt = " ".join(a[::-1])  # " " - space as a seperator
    print(rev_txt)


# Password generator
def pass_gen(number):
    char_book = "abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ1234567890!@#4%^&*(){}[]"
    if number == 1:
        print("Your new password is: ", "".join(random.sample(char_book, 8)))
    elif number == 2:
        print("Your new password is: ", "".join(random.sample(char_book, 16)))
    elif number == 3:
        print("Your new password is: ", "".join(random.sample(char_book, 24)))
    else:
        print("You pick a wrong number!")


# Number appearance on the list
def list_app(a_list, num):
    for i in a_list:
        if i == num:
            return True
    return False


# Binary search
def bin_se(a_list, num):
    while len(a_list) > 1:
        if a_list[len(a_list) // 2] > num:  # greater than num
            a_list = a_list[:len(a_list) // 2]
        else:  # smaller than num
            a_list = a_list[len(a_list) // 2:]
    if a_list[0] == num:
        return True
    else:
        return False


# Download a file - only first time
def download(file_name, address):  # file_name with extension
    if not os.path.isfile('/'+file_name):
        url = address
        r = requests.get(url, allow_redirects=True)
        open(file_name, 'wb').write(r.content)


# Read file line by line
def read_line(file_name):  # file_name with extension
    dict_count = {}
    with open(file_name, 'r') as open_file:
        line = open_file.readline()
        while line:
            line = line.strip()
            if line in dict_count:
                dict_count[line] += 1
            else:
                dict_count[line] = 1
            line = open_file.readline()
    return dict_count


# Draw a game board - my solution
def draw_board(x, y):
    for i in range(1, x + 1, 1):
        if x == 1 or y == 1:
            print("Board size must be grater than 1!")
            break
        if i == 1:
            for z in range(1, y + 1, 1):
                if z < y:
                    print(" ---", end='')
                else:
                    print(" ---", end='\n')
            for v in range(1, y + 1, 1):
                if v == 1:
                    print("|   |", end='')
                elif v < y:
                    print("   |", end='')
                else:
                    print("   |", end='\n')
            for w in range(1, y + 1, 1):
                if w < y:
                    print(" ---", end='')
                else:
                    print(" ---", end='\n')
        else:
            for v in range(1, y + 1, 1):
                if v == 1:
                    print("|   |", end='')
                elif v < y:
                    print("   |", end='')
                else:
                    print("   |", end='\n')
            for w in range(1, y + 1, 1):
                if w < y:
                    print(" ---", end='')
                else:
                    print(" ---", end='\n')


# Guessing the number - simple guess bot
def guess_bot():
    number = 50
    lst = list(range(1, 100 + 1, 1))
    counter = 0
    while len(lst) > 1:
        counter += 1
        answer = input("Is it " + str(number) + "? (Y/N)")
        if answer.lower() == "y":
            print("I win! And need only " + str(counter) + " guess. That was easy ;)")
            break
        else:
            answer = input("Is Your number (H)igher or (L)ower than: " + str(number))
            if answer.lower() == "h":
                number += 1
            else:
                number -= 1


# Checking the game board for Tic Tac Toe
def check(game_1):
    lst = [0, 0]

    for i in range(3):
        for z in range(3):
            # row
            if game_1[i][0] == "X" and game_1[i][1] == "X" and game_1[i][2] == "X":
                lst = [1, 0]
                break
            # row
            elif game_1[i][0] == "O" and game_1[i][1] == "O" and game_1[i][2] == "O":
                lst = [0, 1]
                break
            # column
            elif game_1[0][i] == "X" and game_1[1][i] == "X" and game_1[2][i] == "X":
                lst = [1, 0]
                break
            # column
            elif game_1[0][i] == "O" and game_1[1][i] == "O" and game_1[2][i] == "O":
                lst = [0, 1]
                break
            # diagonals
            elif game_1[0][0] == game_1[1][1] == game_1[2][2] == "X" or game_1[0][2] == game_1[1][1] \
                    == game_1[2][0] == "X":
                lst = [1, 0]
                break
            elif game_1[0][0] == game_1[1][1] == game_1[2][2] == "O" or game_1[0][2] == game_1[1][1] \
                    == game_1[2][0] == "O":
                lst = [0, 1]
                break
            else:
                lst = [1, 1]

    result(lst)


# Printing the result for Tic Tac Toe
def result(lst):
    if lst[0] == 1 and lst[1] == 0:
        print("Player One wins!")
    elif lst[1] == 1 and lst[0] == 0:
        print("Player Two wins!")
    elif lst[0] == 1 and lst[1] == 1:
        print("It's a tie!")
    else:
        print("Something went wrong!")

    print(lst)


# Tic Tac Toe game
def game_ttt():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    print("Let's the game begin. \n")
    i = 0
    while True:
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            player = "One"
            sign = "X"
        else:
            player = "Two"
            sign = "O"
        print(game[0])
        print(game[1])
        print(game[2])
        if i == 9:
            break
        i += 1
        while True:
            while True:
                user_one = str(
                    input("Player " + player + " where You want to place '" + sign +
                          "'? (row,col) - accepted numbers from 1 to 3: \n"))
                if "," in user_one:
                    usr_cor = user_one.split(",")
                    usr_row = int(usr_cor[0].strip()) - 1
                    usr_col = int(usr_cor[1].strip()) - 1
                    if usr_col > 2 or usr_col < 0 or usr_row > 2 or usr_row < 0:
                        print("Your coordinates are out of range, please choose another")
                    else:
                        if game[usr_row][usr_col] == 0:
                            game[usr_row][usr_col] = sign
                            break
                        else:
                            print("This cell is non-available, please choose another")

                else:
                    print("Wrong coordinates format - try again")
            break
    print("Game Over")


# Max of 3
def max_3(a, b, c):
    if a > b and a > c:
        print("Largest number is: " + a)
    elif b > c and b > a:
        print("Largest number is: " + b)
    else:
        print("largest number is: " + c)


# Create blank word for Hangman Game
def blank(word):
    disp = ''
    for i in range(0, len(word)):
        disp = disp + '_'
    return disp


# Core of Hangman Game
def hangman_game(word, disp):
    counter = 0
    test = True
    while test:
        draw_hangman(counter)
        if counter == 6:
            break
        print(disp)
        letter = input('Guess Your letter: ').upper()
        for i in range(0, len(word)):
            if '_' in disp:
                disp = list(disp)
                if letter not in word:
                    print("Incorrect letter")
                    counter += 1
                    disp = ''.join(disp)
                    break
                if letter in word[i]:
                    if letter not in disp[i]:
                        disp[i] = word[i]
                    else:
                        print("You already use this letter")
                        disp = ''.join(disp)
                        break
                disp = ''.join(disp)
            else:
                print(word, end="\n")
                print("You won!")
                test = False
                break
    print("Game Over")
    print(word)


# Draw a hangman guy
def draw_hangman(error):
    if error == 0:
        print("   ________\n"
              "  |       |\n"
              "  |\n"
              "  |\n"
              "  |\n"
              "  |\n"
              "__|__\n")
    elif error == 1:
        print("   ________\n"
              "  |       |\n"
              "  |       O\n"
              "  |\n"
              "  |\n"
              "  |\n"
              "__|__\n")
    elif error == 2:
        print("   ________\n"
              "  |       |\n"
              "  |       O\n"
              "  |       |\n"
              "  |       |\n"
              "  |\n"
              "__|__\n")
    elif error == 3:
        print("   ________\n"
              "  |       |\n"
              "  |       O\n"
              "  |      \|\n"
              "  |       |\n"
              "  |\n"
              "__|__\n")
    elif error == 4:
        print("   ________\n"
              "  |       |\n"
              "  |       O\n"
              "  |      \|/\n"
              "  |       |\n"
              "  |\n"
              "__|__\n")
    elif error == 5:
        print("   ________\n"
              "  |       |\n"
              "  |       O\n"
              "  |      \|/\n"
              "  |       |\n"
              "  |      /\n"
              "__|__\n")
    elif error == 6:
        print("   ________\n"
              "  |       |\n"
              "  |       O\n"
              "  |      \|/\n"
              "  |       |\n"
              "  |      / \ \n"
              "__|__\n")


# Make a dict for hangman
def dict_create():
    download('dict.txt', 'http://norvig.com/ngrams/sowpods.txt')

    words = []

    with open('dict.txt', 'r') as text:
        line = text.readline().strip()
        words.append(line)
        while line:
            line = text.readline().strip()
            words.append(line)
    return words


# Random word from dict
def random_word(words):
    random_num = random.randint(0, len(words))
    return words[random_num]
