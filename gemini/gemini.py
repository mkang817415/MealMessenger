import sys 
import os 
from dotenv import load_dotenv
import google.generativeai as genai


from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def connect_gemini(): 
   sys.path.append('../')
   load_dotenv() 

   GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
   genai.configure(api_key=GEMINI_API_KEY)
   
   model = genai.GenerativeModel('gemini-1.5-flash')
   return model

def generate_prompt(menus: str): 
      model = connect_gemini()
      
      script_dir = os.path.dirname(__file__)  
      menu_prompt_path = os.path.join(script_dir, 'menu_prompt.txt')  
      
      with open(menu_prompt_path, 'r') as f: 
         menu_prompt = f.read()
            
      response = model.generate_content(menu_prompt + menus)
      return response.text
   
# print(generate_prompt("sjdfsd"))