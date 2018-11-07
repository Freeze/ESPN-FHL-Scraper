#!/usr/bin/env python3
import sys, os
import csv, json
from time import sleep
#from selenium import webdriver
#from bs4 import BeautifulSoup
#from selenium.webdriver.firefox.options import Options

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

#URL = os.getenv('FH_URL')

LEAGUE_URL = os.getenv('LEAGUE_URL')
URL_BASE = os.getenv('FH_URL')

def write_to_csv(data_list,file_name):
  csv_file = open(file_name, 'w')
  csvwriter = csv.writer(csv_file)
  csvwriter.writerows(data_list)
  csv_file.close()

def get_player_names(page):
  soup=BeautifulSoup(page, "lxml")
  player_names = soup.find_all('a', class_="link clr-link pointer")
  return player_names

def get_player_info(page):
  soup=BeautifulSoup(page, "lxml")
  player_info = soup.find_all('tr', class_="Table2__tr Table2__tr--lg Table2__odd")
  return player_info

def get_team_name(page):
  soup=BeautifulSoup(page, "lxml")
  team_name = soup.find('span', class_="teamName truncate")
  return team_name

def get_league_rosters(page):
  soup = BeautifulSoup(page,"lxml")
  teams = soup.find_all('div', class_='InnerLayout__child flex pa1 bg-clr-white br-5')
  for team in teams:
    team_info = team.find_all('tr', class_='Table2__tr Table2__tr--sm Table2__odd')
    team_name = team.find('span', class_='teamName truncate')
    players = team.find_all('a', class_='link clr-link pointer')
    print(team_name.text)
    for player in players:
      print(player.text)
    print('\n')

def load_page(page):
  opts = Options()
  opts.binary=r"C:\Program Files\Mozilla Firefox\firefox.exe"
  opts.profile=webdriver.FirefoxProfile('C:\\Users\\Holden\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\6eyircz4.Selenium')
  opts.headless = True
  browser = webdriver.Firefox(options=opts)
  browser.get(page)
  sleep(15)
  page_source = browser.page_source
  print("Closing browser.  Headless is silly")
  browser.quit()
  return(page_source)

package_list = ['selenium','bs4']

for package in package_list
  install_and_import(package)

data = load_page(LEAGUE_URL)
get_league_rosters(data)

#team = load_page(URL_BASE)
#player_names = get_player_names(team)
#team_name = get_team_name(team)


#player_names.insert(0,team_name)
#write_to_csv(player_names, "player_names.csv")
