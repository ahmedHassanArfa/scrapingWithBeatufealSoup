from builtins import print

import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page2 = requests.get("https://ar.wikipedia.org/wiki/%D8%A7%D9%84%D8%B5%D9%81%D8%AD%D8%A9_%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D9%8A%D8%A9")
page3 = requests.get("https://www.expedia.com/vacation-rentals/")

page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(page2.content, 'html.parser')
soup.find_all('p')

for item in list(soup.find_all('p')):
    print(item.get_text())
    print('\n')

# for item in list(soup.select('p')):
#     print(item.get_text())
#     print('\n')