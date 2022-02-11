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
        # rows & columns
        if game_1[i][0] == game_1[i][1] == game_1[i][2] == 1 or game_1[0][i] == game_1[1][i] == game_1[2][i] == 1:
            lst = [1, 0]
        elif game_1[i][0] == game_1[i][1] == game_1[i][2] == 2 or game_1[0][i] == game_1[1][i] == game_1[2][i] == 2:
            lst = [0, 1]
        # diagonals
        elif game_1[0][0] == game_1[1][1] == game_1[2][2] == 1 or game_1[0][2] == game_1[1][1] == game_1[2][0] == 1:
            lst = [1, 0]
        elif game_1[0][0] == game_1[1][1] == game_1[2][2] == 2 or game_1[0][2] == game_1[1][1] == game_1[2][0] == 2:
            lst = [0, 1]
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

