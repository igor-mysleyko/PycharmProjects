from selenium import webdriver
import time
import lxml
from bs4 import BeautifulSoup
import requests

import sqlite3






headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

args = []


for count in range(1,10):
    url=f'https://cars.av.by/filter?page={count}&sort=4'
    r = requests.get(url=url, headers=headers)



    soup=BeautifulSoup(r.text,'lxml')
    auto_card=soup.find_all('div',class_='listing-item__wrap')

    for auto in auto_card:

        url=f'https://cars.av.by{auto.find("a").get("href")}'
        title=auto.find('span','link-text').text.strip()
        cost=auto.find('div','listing-item__priceusd').text.strip()
        date=auto.find('div','listing-item__date').text.strip()
        if date=='час назад' or date=='2 часа назад':
            break
        args.append((url,date,title,cost))


conn = sqlite3.connect("mydata.db")

cursor = conn.cursor()


cursor.executemany("INSERT INTO books VALUES (?,?,?,?)",args)
conn.commit()
conn.close()






