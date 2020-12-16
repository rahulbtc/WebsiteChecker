# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:46:55 2020
@author: rahul
Note: This is the code if you want to build a windows App. I have used TKinter
module for the desktop GUI. (It is just a basic fancy thing which just seemes to
be working for my use case. There may be bugs)
Feel free to replicate this code, and compile it with PyInstaller to make your .exe
file.
Here's a very nice article which I stumbled upon, might help you out if you are a beginner.

"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 02:58:20 2020

@author: rahul
"""
from tkinter import*
import os
import urllib
import requests
from contextlib import suppress
import time


os.system('clear')
# site = "https://www.google.com"

def telegram_bot_sendtext(bot_message):
   endpt = 'https://api.telegram.org/bot'
   bot_token = '1301415216:AAHO2QF7FZOJ4mTxBeF02lL19w7-BQhm3lA'
   action = '/sendMessage?chat_id='
   bot_chatID = '@websitechecktest'
   mode = '&parse_mode=Markdown&text='
   
   send_text = endpt + bot_token + action + bot_chatID + mode + bot_message
   response = requests.get(send_text)
   return response.json()

def hello():
    global site
    site = mytext.get()
    print(site)
    with suppress(Exception):  ## https://hg.python.org/cpython/rev/406b47c64480 
        while (1):
            try:
                x = (urllib.request.urlopen(site).getcode())  
                ## Will return 200 if status = OK
                if x == 200:
                        print("Connected successfully. Sent message to telegram")
                        s = f"Connected Successfully to {site}"
                        telegram_bot_sendtext(s)
                        show_text = Label(root, text = s)
                        show_text.pack()
                        break
                else:
                    print("Something is wrong")
            except:
                e="Trying again"
                print(e)
                show_e = Label(root, text = e)
                show_e.pack()
                time.sleep(1)
                continue

root = Tk()
root.title('Windows Test app')
root.geometry("300x200")
mylabel = Label(root, text = "Enter the website: ")
mylabel.pack()

mytext = Entry(root, width = 30)
mytext.pack()

mybutton = Button(root, text = "Submit", command=hello) #This is a function
mybutton.pack()

root.mainloop()

