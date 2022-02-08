import random

g_num = random.randint(1, 9)
counter = 0
while True:
    counter += 1
    user_num = input("Please, guess a number: ")
    if user_num == "exit":
        break
    elif int(user_num) < g_num:
        print("Your guess is to low... Try again or if want to stop type: exit")
    elif int(user_num) > g_num:
        print("Your guess is to high... Try again or if want to stop type: exit")
    else:
        print("That's it! You guess a number!")
        print("You need ", counter, " guesses to guess the number!")
        break
print("Game Over")
