global webhook,scraper_api_key,characters
webhook = 'WEBHOOK'
scraper_api_key = 'KEY'
characters = 8
#code
import requests,time
from lib___123 import preview
from lib___123 import version
from random import randint
from dhooks import Webhook
import threading
from colorama import Fore, Back, init
init()
print(preview)
hook = Webhook(webhook)


def createPayload(method: str, url: str, data = None):
    payload = { 'api_key': scraper_api_key, 'url': url } 
    r = None
    if method == "get":
        r = requests.get('https://api.scraperapi.com/', params=payload)
    elif method == "post":
        r = requests.post('https://api.scraperapi.com/', params=payload, data=data)
    return r

def randomURL():
    abc = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    lenght = len(abc) - 1
    url = ''
    for i in range(characters):
        url += abc[randint(0,lenght)]
    return url

count = 1
def createSearch():
    global count
    while 1:
        #time.sleep(.1)
        randomstr = randomURL()
        try:
            url = createPayload(method = 'get', url = f'https://discord.com/api/v9/invites/{randomstr}')
            if url.status_code == 200:
                print(f'\n[+] ' + Back.GREEN + str(url.status_code) + Back.RESET + f' | {randomstr}\n')
                hook.send(f'https://discord.com/invite/{randomstr}')
            elif url.status_code == 404:
                print(f'[{str(count)}] ' + Back.RED + str(url.status_code) + Back.RESET + f' | {randomstr}')
                count+=1
            elif url.status_code == 429:
                print('rate limit')
        except:
            pass

def start(times = 1):
    for i in range(times):
        th = threading.Thread(target=createSearch)
        th.start()

start(5)
