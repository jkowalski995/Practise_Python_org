import requests
from bs4 import BeautifulSoup
import os

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
# print(r_html)
soup = BeautifulSoup(r_html, features="html.parser")

# os.chdir('/home/jakub/PycharmProjects/practise_python/Exercise_19')
# x = open('soup', 'wt')
# x.write(soup.prettify())
# x.close()

find = soup.find_all('p')  # find all tags with h3

# os.chdir('/home/jakub/PycharmProjects/practise_python/Exercise_19')
# x = open('find', 'wt')
# x.write(str(find))
# x.close()

n = len(find)  # get len for iteration
for x in range(6, n-5):  # 6 and -5 to cut some stuff
    print(str.strip(find[x].text))  # strip everything non-text

