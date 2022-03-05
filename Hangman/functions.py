import random, os, requests


# Download a file - only first time
def download(file_name, address):  # file_name with extension
    if not os.path.isfile('/'+file_name):
        url = address
        r = requests.get(url, allow_redirects=True)
        open(file_name, 'wb').write(r.content)


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
