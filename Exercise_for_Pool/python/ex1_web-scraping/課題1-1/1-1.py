from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://r.gnavi.co.jp/area/tokyo/izakaya/rs/?sort=LOW'

r = requests.get(url)
r.raise_for_status()

soup = BeautifulSoup(r.content, 'lxml')

food_stores =  soup.find_all('div', class_='style_restaurant__SeIVn')

d_list = []

for food_store in food_stores:
    store_name = food_store.find('h2', class_='style_restaurantNameWrap__wvXSR').text
    page_url = food_store.find('a').get('href')

#     print(store_name)
#     print(page_url)
    
    page_r = requests.get(page_url)
    page_r.raise_for_status()
    
    page_soup = BeautifulSoup(page_r.content, 'lxml')
    
    store_summary = page_soup.find('div', id='info-table')
    
    for table_row in store_summary.find_all('tr'):       
        phone_number  = table_row.select_one("#info-phone > td > ul:nth-child(1) > li:nth-child(1) > span.number")
        location = table_row.select_one('#info-table > table > tbody > tr:nth-child(3) > td > p > span.region')
        url = table_row.select_one('#info-table > table > tbody > tr:nth-child(11) > td > ul > li:nth-child(1) > a')
        
        print(company_name)
        print(type(phone_number))
        print(location)
        print(url)
        