#!/usr/local/bin/python3
import sys, os
import csv, json
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = os.getenv('FH_URL')

#options = Options()
#options.add_argument("--headless")

#browser = webdriver.Firefox(options=OPTIONS)
browser = webdriver.Firefox()

browser.get(URL)

sleep(10)

source = browser.page_source

soup = BeautifulSoup(source, "lxml")

rows = soup.find_all('tr', class_="Table2__tr Table2__tr--lg Table2__odd")

rows = soup.find_all('a', class_="link clr-link pointer")

players = rows[1].find_all('span')

for x in rows:
    print(x.text)
