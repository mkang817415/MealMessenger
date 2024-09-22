'''SMS connection to Twilio API'''

import os
import sys
from dotenv import load_dotenv
import datetime 

from twilio.rest import Client

from gemini.gemini import *
from menu_scraping.processing import *
from menu_scraping.menu_models import * 


def twilio_connection(): 
    load_dotenv() 
    
    # Gathering Credentials
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    return client 

def send_message(message: str, sender='+18777194154', receiver='+18187952054'): 
    client = twilio_connection()
     
    message = client.messages \
                        .create(
                            body = message, 
                            from_=sender, 
                            to=receiver
                        )
    if not message.sid: 
        return False
    return message.sid

def send_menu(menu: str): 
    today = datetime.datetime.today().strftime('%m-%d-%Y')

    
    meal = meal_timer()
    
    recap = generate_prompt(menu[0] + menu[1])
    message = f"{today}'s {meal} menu is: \n \n {menu[0]} \n \n {menu[1]} \n \n"
    
    message += f"{meal} recap: \n {recap}" 
    return message

if __name__ == '__main__':
    menu = get_menu()
    message = send_menu(menu)
    
    send_message(message, receiver='+18187952054')
    send_message('whats up minj this is ming', receiver='+18187952054')