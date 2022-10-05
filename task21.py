import requests
from bs4 import BeautifulSoup


def write_file(name:  str, array: list) -> None:
    with open(name, 'w') as open_file:
        for elements in array:
            open_file.write(elements)
            open_file.write('\n')
    return


url = 'https://www.nytimes.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.findAll('h3')
articles = []
for text in title:
    articles.append(text.contents[0])

filename = input('Enter your file name ') + '.txt'

write_file(filename, articles)
