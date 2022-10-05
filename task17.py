# task №17
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.findAll('h3')
articles = []
for txt in title:
    articles.append(txt.contents[0])

print(articles)
