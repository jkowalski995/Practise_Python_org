import random

# common numbers function for Exercise_5
def common(a_list,b_list):
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
        if num % i == 0: list_p += [i]
        i += 1
    if num == 1:
        print("Number ", num, " is prime!")
    elif len(list_p) == 2:
        print("Number ", num, " is prime!")
    else:
        print("Number ", num, " is not prime...")

# list beginning and ending
def beg_end(a_list):
    new_list = []
    new_list.append(a_list[0])
    new_list.append(a_list[len(a_list)-1])
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

