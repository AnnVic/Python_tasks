import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.findAll('h3')
articles = []
for txt in title:
    articles += [txt.contents[0]]

with open('article.txt', 'w') as open_file:
    for i in articles:
        open_file.write(i)
        open_file.write('\n')

# solution: ask the user to specify the name of the output file
filename = input('Enter your file name ') + '.txt'
with open(filename, 'w') as open_file:
    for i in articles:
        open_file.write(i)
        open_file.write('\n')
