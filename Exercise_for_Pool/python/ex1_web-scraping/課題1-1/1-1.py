#完成版
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://r.gnavi.co.jp/area/tokyo/izakaya/rs/?sort=LOW&p={}.format()'
max_page_index(3)
d_list = []
for i in range(max_page_index):
    acccess_url = url.format(i+1)

    r = requests.get(acccess_url)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')

    food_stores =  soup.find_all('div', class_='style_restaurant__SeIVn')

    for food_store in food_stores:
        page_url = food_store.find('a').get('href')

        page_r = requests.get(page_url, timeout=3)
        page_r.raise_for_status()

        page_soup = BeautifulSoup(page_r.content, 'lxml')

        store_name = page_soup.select_one('#info-name').text

        phone_number = page_soup.select_one('#info-phone > td > ul > li:nth-child(1) > span.number').text


        store_building = page_soup.select_one('#info-table > table > tbody > tr:nth-child(3) > td > p > span.locality')

        if store_building:
            building_name = store_building.text
        else:
            building_name = ''


        store_address = page_soup.select_one('#info-table > table > tbody > tr:nth-child(3) > td > p > span.region').text
        
        def divide_addess(address):
            matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address)
            store_address1 = matches[1]
            store_address2 = matches[2]
            store_address3 = matches[3]



        if __name__ == '__main__':
            address = store_address
            divide_addess(address)


    options = Options()
    options.add_argument("--headless") 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()


    def selenium(page_url):
        driver.get(page_url)
        sleep(3)

        try:
            shop_url_tag = driver.find_element_by_css_selector(
                '#info-table > table > tbody > tr:nth-child(9) > td > ul > li > a'
            )
            shop_url = shop_url_tag.get_attribute("href")
        except Exception as e:
            shop_url = ''



    for food_store in food_stores:
        page_url = food_store.find('a').get('href')

        selenium(page_url)




        d_list.append({
            '店舗名':store_name,
            '電話番号':phone_number
            'メールアドレス':''
            '都道府県':address1,
            '市町村':address2,
            '番地':address3,
            '建物名':building_name,
            'URL':selenium(page_url)
            'SSL':SSL
        })


df = pd.DataFrame(d_list)
df.to_csv('sample.csv', index=None, encoding='utf-8-sig')