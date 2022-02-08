import requests
from bs4 import BeautifulSoup
import os

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")

find = soup.find_all('p')  # find all tags with h3

name = input("Please name the file: \n")
os.chdir('/home/jakub/PycharmProjects/practise_python/Exercise_21')

with open(name, 'wt') as f:
    n = len(find)  # get len for iteration
    for x in range(6, n-5):  # 6 and -5 to cut some stuff
        f.write(str.strip(find[x].text))  # strip everything non-text

# with open() as f: is an alternative attempt to writing a file
# alternate way is to do: open_file = open ()
# open_file.write()
# open_file.close()
