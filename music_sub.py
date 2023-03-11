import requests
import urllib.parse
from bs4 import BeautifulSoup
song = str(input())
safe_string = urllib.parse.quote_plus(song)
a = requests.get(f'https://www.google.com/search?q={safe_string}+%D1%82%D0%B5%D0%BA%D1%81%D1%82+%D0%BF%D0%B5%D1%81%D0%BD%D0%B8&client=ucweb-b&channel=sb')
soup = BeautifulSoup(a.text, "html.parser")
allNews = soup.findAll('div', class_='BNeawe tAd8D AP7Wnd')
try:
    print(allNews[3].text)
except IndexError:
    print("Error")

