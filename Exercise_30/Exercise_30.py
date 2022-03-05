from functions import download
import random

download('dict.txt', 'http://norvig.com/ngrams/sowpods.txt')

words = []

with open('dict.txt', 'r') as text:
    line = text.readline().strip()
    words.append(line)
    while line:
        line = text.readline().strip()
        words.append(line)

random_num = random.randint(0, len(words))

print("Random word is: ", words[random_num])
