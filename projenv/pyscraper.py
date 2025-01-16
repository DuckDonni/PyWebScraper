import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
r = requests.get('https://en.wikipedia.org/wiki/Talk:Cat')

print(r)
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_ = 'entry-content')
content = soup.find_all('p')


print(content)