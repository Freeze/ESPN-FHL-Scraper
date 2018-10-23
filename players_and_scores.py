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

#OPTIONS = Options()
#OPTIONS.add_argument("--headless")

#browser = webdriver.Firefox(options=OPTIONS)
browser = webdriver.Firefox()

browser.get(URL)

sleep(10)

SOURCE = browser.page_source

SOUP = BeautifulSoup(SOURCE, "lxml")

ROWS = SOUP.find_all('tr', class_="Table2__td Table2__td--fixed-width")

PLAYERS = ROWS[1].find_all('span')

print(PLAYERS)
