import requests
from bs4 import BeautifulSoup
# import os

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
# print(r_html)
soup = BeautifulSoup(r_html, features="html.parser")

# os.chdir('/home/jakub/PycharmProjects/practise_python/Exercise_17')
# x = open('soup', 'wt')
# x.write(soup.prettify())
# x.close()

h_3 = soup.find_all('h3') # find all tags with h3

# os.chdir('/home/jakub/PycharmProjects/practise_python/Exercise_17')
# x = open('h3', 'wt')
# x.write(str(h_3))
# x.close()

n = len(h_3) # get len for iteration
for x in range(n):
    print(str.strip(h_3[x].text)) # strip everything non-text


