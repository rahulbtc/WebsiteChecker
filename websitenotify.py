# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:03:02 2020
@author: rahul
"""

import urllib
import requests
from contextlib import suppress
import time


site = str(input("Enter website to get alert: "))
# Example: https:www.google.com

def telegram_bot_sendtext(bot_message):
   endpt = 'https://api.telegram.org/bot'
   bot_token = '1********6:AAHO********************9w7-B*****A'
   action = '/sendMessage?chat_id='
   bot_chatID = '@websitechecktest'  # This is my public dummy group.
   mode = '&parse_mode=Markdown&text='
   
   send_text = endpt + bot_token + action + bot_chatID + mode + bot_message
   response = requests.get(send_text)
   return response.json()

with suppress(Exception):  ## https://hg.python.org/cpython/rev/406b47c64480 
    while (1):
        try:
            x = (urllib.request.urlopen(site).getcode())  
            ## Will return 200 if status = OK
            if x == 200:
                    print("Connected successfully. Sent message to telegram")
                    telegram_bot_sendtext(f"Connected Successfully to {site}")
                    break
            else:
                print("Something is wrong")
        except:
            print("Trying again")
            time.sleep(60)
            continue
