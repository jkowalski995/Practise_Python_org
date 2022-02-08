import functions

# Download the files
functions.download('one.txt', 'https://www.practicepython.org/assets/primenumbers.txt')
functions.download('two.txt', 'https://www.practicepython.org/assets/happynumbers.txt')

dict_count = functions.read_line('one.txt')
dict_count_2 = functions.read_line('two.txt')
for i in dict_count:
    if i in dict_count_2:
        print(i)
