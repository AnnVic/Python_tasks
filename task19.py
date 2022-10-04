import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
txt = soup.select('p')
for i in txt:
    print(i.text)
