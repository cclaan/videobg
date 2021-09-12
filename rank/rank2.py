import sys
import re
import random
import os

from random import randint
import datetime

import time
import json 

from bs4 import BeautifulSoup

from selenium import webdriver

from termcolor import colored, cprint




chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('/Users/cc/Downloads/chromedriver', options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


sitename = "freebackgrounderaser.com"

# Wait to fill out captcha ## 

query = 'comprehensive guide to web scraping'
url = "http://www.google.com/search?q=" + query.replace(' ', '+') 
driver.get(url)


while 'search?' not in driver.current_url:
    print(" ... waiting BAD URL: " + driver.getCurrentUrl() ) 
    time.sleep(1)



keywords = [
#"freebackgrounderaser.com",
"free background eraser.com",
"free online background remover",
"free online background eraser",
"free background remover",
"free background eraser",
]

print("|"*200)

results = []

for keyword in keywords:
    
    print('='*80)
    print(f"{keyword:>40}")

    links = [] 
    start = 0 
    NUM_PAGES = 4 # * 100 = 400 RESULTS
    for page_idx in range(NUM_PAGES):

        query_url = 'https://www.google.com/search?num=100&nfpr=1&q=' + keyword.replace(" ", "+")

        if start > 0:
            query_url += f"&start={start}"

        driver.get(query_url)

        time.sleep( random.uniform(1.5, 5.5) )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_="yuRUbf")

        for i,h in enumerate(search):
            links.append( h.a.get('href') )

        num_results = len(search)
        
        print(f"  - page {page_idx:<5}  start: {start:<5}  results: {num_results:<5}  - total: {len(links):<5}")
        
        start += num_results

        #print(f"   Start - {start}  links: {len(links)} ")
        if num_results < 50:
            print( " -- break not enough results ")
            break
    







    # starts = [0, 100]

    # for start in starts:
    #     query_url = 'https://www.google.com/search?num=100&nfpr=1&q=' + keyword.replace(" ", "+")

    #     if start > 0:
    #         query_url += f"&start={start}"

    #     print("   Query: " + query_url)

    #     driver.get(query_url)

    #     time.sleep( random.uniform(1.5, 5.5) )

    #     soup = BeautifulSoup(driver.page_source, 'html.parser')
    #     search = soup.find_all('div', class_="yuRUbf")

    #     for i,h in enumerate(search):
    #         links.append( h.a.get('href') )

    #     print(f"   Start - {start}  links: {len(links)} ")


    # print(f"got {len(links)} links")

    rank = "not ranked"
    for i, l in enumerate(links):
        if sitename.lower() in l.lower():
            #print(f"Found link at position: {i:5}:\n   {l} ")
            cprint(f"Found link at position: {i:5} / {len(links):5}    :    {keyword:<50} ", 'white', 'on_red')


            rank = i
            break
    
    now_str = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    results.append( {"keyword" : keyword, "rank" : rank, "date" : now_str } )

json_name = "keywords_" + datetime.datetime.now().strftime("%d-%m-%Y__%H_%M_%S") + ".json"

json.dump(results, open(os.path.join("results", json_name), "w"), indent=True, sort_keys=True)


