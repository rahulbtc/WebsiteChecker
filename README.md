# WebsiteChecker
A sample program to get telegram alerts when a website starts working again. (Http 200 status code)

Requirements:
1) Python 3.4+
2) Libraries:
     a) urllib     (https://docs.python.org/3/library/urllib.html#module-urllib)
     b) requests   (https://requests.readthedocs.io/en/master/)
     c) contextlib (https://docs.python.org/3/library/contextlib.html)
                  

How to get Telegram API: 
1) Open Telegram, search for @Botfather and press start
2) Click on the /newbot command in the chat
3) Follow the instructions on the botfather to name your bot and you will get a new bot and an API key.
4) Create a new dummy public group and name it (I created one for fun)
5) Add your telegram bot to the group.
6) Paste the api keys in the code.
7) Run the program.

    
Optional: I have not used the telegram libraries for Python. In case you want to use them
          instead, please feel free to try out in your own way.
          Here's a nice tutorial in case you want to try on:
          https://www.geeksforgeeks.org/send-message-to-telegram-user-using-python/
          

--------------------------------------------------------------------------------------------------------------------------------------------------------------
Reason why I created this:
I was trying to open a website, which was not under maintenance, so it was not running. 
So instead of checking my browser every time to see when the website comes up, I created this
simple program to notify me on telegram once the website comes back.
Of course the agenda of the program was mostly fun and for educational purposes only.
(P.s. The site was not opening for a couple of days, and I kept it running on my Raspberry Pi, and got notification as expected when site came back online)

