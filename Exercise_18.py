import random


def cows_bulls(number, g_number):
    cow_bul = [0, 0]
    for i in range(len(number)):
        if number[i] == g_number[i]:
            cow_bul[0] += 1
        else:
            cow_bul[1] += 1
    print("Cows ", cow_bul, " Bulls")
    return cow_bul


def main():
    num = str(random.randint(0, 9999))
    print("Welcome in cows&bulls game!"
          "Please type your guess"
          "In order to stop a game type exit")
    guess_counter = 0
    while True:
        guess_counter += 1
        user_input = input()
        if user_input.lower() == "exit":
            break
        else:
            result = cows_bulls(user_input, num)

        if result[0] == 4:
            print("You guessed the number")
            print("You need only ", guess_counter, " guesses")
            break


if __name__ == "__main__":
    main()
