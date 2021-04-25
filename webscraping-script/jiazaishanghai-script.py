#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:37:42 2021

@author: lescardone
"""

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import re

url = 'http://jiazaishanghai.com/House/Search'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

# advanced settings -- no real estate agents
time.sleep(5)

button = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[8]/div/i')
button.click()

time.sleep(2)
select = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[7]/div[5]/ul/li[1]')
select.click()

time.sleep(2)
select2 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div/div[7]/div[5]/ul/li[2]')
select2.click()

soup = BeautifulSoup(driver.page_source, 'lxml')
page = soup.find('div', class_ = 'const_lt')
listings = page.find_all('li',class_='clearfix')
listings

columns = ['district', 'complex_name', 'rental_period', 'use_type', 'building_type', 'floor', 'layout', 'sqmeters', 'address', 'price','amenities', 'descript']
df = pd.DataFrame(columns=columns) 
df2 = pd.DataFrame(columns=columns) 

for i in range(180):
    
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height
    
    time.sleep(2)
    button = driver.find_element_by_class_name('layui-laypage-next')
    button.click()
    print(i)
    
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    page = soup.find('div', class_ = 'const_lt')
    listings = page.find_all('li',class_='clearfix')
    
    for idx,apt in enumerate(listings):
            
            # get listing link
            link = apt.find('a')['href']
            link
            tab = 'http://jiazaishanghai.com' + link
            
            # open new tab
            driver.execute_script(f'''window.open('{tab}','_blank');''')
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            #driver.refresh()
            
            for x in range(5):
                try:
                    # pull html
                    apt_soup = BeautifulSoup(driver.page_source,'lxml')
                    
                    # address
                    add = apt_soup.find('title').text
                    add = add.split('\n')
                    address = add[0]
        
                    # item list (8)
                    # district, complex, rental period, use type, building type, floor, layout, sqmeters
                    cells = apt_soup.find('div',class_='row row2').find_all('p')
                    cell_list = [cell.text for cell in cells]
                    items = [item.split('：')[1] for item in cell_list[:-1]]
            
                    # append address (9)
                    items.append(address)
            
                    # add price (10)
                    price = apt_soup.find('span',class_='houseprices').text
                    items.append(price)
            
                    # amenities (11)
                    table2 = apt_soup.find('ul',class_='tubiao_list clearfix')
                    ammens = table2.find_all('p')
                    ammens_list = [ammen.text for ammen in ammens]    
                    items.append(ammens_list)
                    # print(items)
            
                    # descript (12)
                    descript = apt_soup.find('div',class_='gj_jianjie').text
                    descript_clean = re.findall(r"[\w]+",descript)
                    items.append(descript_clean)
                    print(len(items),idx,i)
                    print(x)
                    break
                
                except AttributeError:
                    time.sleep(5)
                    continue
                
            # append to df
            length = len(df2)
            if len(items) == 12:
                df2.loc[length] = items
            else:
                pass
            
            # close tab and switch back
            driver.close()
            driver.switch_to.window(driver.window_handles[0])    
            df2.to_csv('jiazaishanghai.csv')
            # driver.quit()
      
    

for i in range(5):
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    page = soup.find('div', class_ = 'const_lt')
    listings = page.find_all('li',class_='clearfix')
    
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height
    
    time.sleep(3)
    button = driver.find_element_by_class_name('layui-laypage-next')
    button.click()
    print(i)
    continue   


'''
            # address
            add = apt_soup.find('title').text
            add = add.split('\n')
            address = add[0]
        
            # item list (8)
            # district, complex, rental period, use type, building type, floor, layout, sqmeters
            cells = apt_soup.find('div',class_='row row2').find_all('p')
            cell_list = [cell.text for cell in cells]
            items = [item.split('：')[1] for item in cell_list[:-1]]
            
            # append address (9)
            items.append(address)
            
            # add price (10)
            price = apt_soup.find('span',class_='houseprices').text
            items.append(price)
            
            # amenities (11)
            table2 = apt_soup.find('ul',class_='tubiao_list clearfix')
            ammens = table2.find_all('p')
            ammens_list = [ammen.text for ammen in ammens]    
            items.append(ammens_list)
            # print(items)
            
            # descript (12)
            descript = apt_soup.find('div',class_='gj_jianjie').text
            descript_clean = re.findall(r"[\w]+",descript)
            items.append(descript_clean)
            print(len(items),idx,i)
                   
'''