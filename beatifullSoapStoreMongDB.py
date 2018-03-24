from builtins import print

import requests
from pymongo import MongoClient

from storeSourceItemsToDB import storeSourceItemsToDB
from storeTargetItemsToDB import storeTargetItemsToDB

client = MongoClient('localhost', 27017)
db = client.scrapingDB;

webSite = "https://www.jumia.com.eg"

pageSource = requests.get("https://www.jumia.com.eg/all-products/?utm_campaign=31&utm_medium=affiliation&utm_source=cake&utm_term=569504d9eb5c4")
pageTarget = requests.get("https://www.jumia.com.eg/ar/all-products/?utm_campaign=31&utm_medium=affiliation&utm_source=cake&utm_term=569504d9eb5c4")

allUrls = []

from bs4 import BeautifulSoup
soupSource = BeautifulSoup(pageSource.content, 'html.parser')
soupTarget = BeautifulSoup(pageTarget.content, 'html.parser')
soupSource.find_all('p')

# source texts
order = 1
storeSource = storeSourceItemsToDB()

# scrap the first page
itemsList = soupSource.find_all()
storeSource.storeSourceItemsToDB(itemsList, order, db, webSite);

def followSourceLinks(links):
    for link in links:
        url = link['href']
        if "jumia.com" not in url:
           continue
        if allUrls.count(url) > 0:
            continue
        else:
            allUrls.append(url)
        page = requests.get(url)
        followSourceSoup = BeautifulSoup(page.content, 'html.parser')
        itemsList = followSourceSoup.find_all()
        storeSource.storeSourceItemsToDB(itemsList, order, db, webSite)
        subLinks = followSourceSoup.find_all('a', href=True)
        followSourceLinks(subLinks)
    return

# get all links
firstLinks = soupSource.find_all('a', href=True)
followSourceLinks(firstLinks)


# target Texts
order = 1
storeTarget = storeTargetItemsToDB()

#scrap the first page
itemsList = soupTarget.find_all()
storeTarget.storeTargetItemsToDB(itemsList, order, db, webSite);

def followTargetLinks(links):
    for link in links:
        url = link['href']
        if "jumia.com" not in url:
            continue
        if allUrls.count(url) > 0:
            continue
        else:
            allUrls.append(url)
        page = requests.get(url)
        followTargetSoup = BeautifulSoup(page.content, 'html.parser')
        itemsList = followTargetSoup.find_all()
        storeSource.storeSourceItemsToDB(itemsList, order, db, webSite)
        subLinks = followTargetSoup.find_all('a', href=True)
        followTargetLinks(subLinks)
    return

# get all links
firstLinks = soupSource.find_all('a', href=True)
followTargetLinks(firstLinks)

# for item in list(soup.select('p')):
#     print(item.get_text())
#     print('\n')