import os.path

import requests

# Download a names list file - only first time
if not os.path.isfile('/names.txt'):
    url = 'https://www.practicepython.org/assets/nameslist.txt'
    r = requests.get(url, allow_redirects=True)
    open('names.txt', 'wb').write(r.content)

# Download an images list file - only first time
if not os.path.isfile('/images.txt'):
    url = 'https://www.practicepython.org/assets/Training_01.txt'
    r = requests.get(url, allow_redirects=True)
    open('images.txt', 'wb').write(r.content)

# Counting the names
dict_count = {}
with open('names.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line in dict_count:
            dict_count[line] += 1
        else:
            dict_count[line] = 1
        line = open_file.readline()
print(dict_count)

# Counting the images categories
dict_count_im = {}
with open('images.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line[3:-26]  # cut 3 chars in front and 26 from back, so it gives us a category name
        if line in dict_count_im:
            dict_count_im[line] += 1
        else:
            dict_count_im[line] = 1
        line = open_file.readline()
print(dict_count_im)

# dict_count.keys()
# dict_count.values()

# Be careful with looping!

