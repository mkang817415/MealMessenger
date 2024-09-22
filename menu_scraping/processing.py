import selenium  
import requests
import datetime 

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Glolbal variables 
MEALS = ['Breakfast', 'Lunch', 'Dinner'] 
TIMES = [8, 12, 14]
DINING_HALLS = ['Thorne', 'Moulton Union']
BOWDOIN_MENU_URL = 'https://www.bowdoin.edu/dining/menus/index.html'

def get_menu():
   driver = webdriver.Chrome()
   driver.get(BOWDOIN_MENU_URL)
   
   try: 
      thorne_element = driver.find_element(By.ID, 'u49')
      moulton_element = driver.find_element(By.ID, 'u48')
   except Exception as e: 
      print(e)
      driver.quit() 
      exit()
      return None
   
   thorne_menu = thorne_element.text
   moulton_menu = moulton_element.text
   
   return thorne_menu, moulton_menu

def meal_timer(): 
   current_time = datetime.datetime.now()
   current_hour = current_time.hour
   
   meal_times = {
        TIMES[0]: MEALS[0],
        TIMES[1]: MEALS[1],
        TIMES[2]: MEALS[2],
    }
   
   default_meal = 'Closed'
   return meal_times.get(current_hour, default_meal)


