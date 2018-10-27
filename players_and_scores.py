#!/usr/local/bin/python3
import sys, os
import csv, json
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Method list
def write_to_csv(data_list,file_name):
    
   csv_file = open(file_name, 'w')  
    
   csvwriter = csv.writer(csv_file)

   csvwriter.writerows(data_list)

   csv_file.close()


URL = os.getenv('FH_URL')

browser = webdriver.Firefox()

browser.get(URL)

sleep(15)

source = browser.page_source

soup = BeautifulSoup(source, "lxml")

player_info = soup.find_all('tr', class_="Table2__tr Table2__tr--lg Table2__odd")

player_names = soup.find_all('a', class_="link clr-link pointer")

write_to_csv(rows, "player_names.csv")


