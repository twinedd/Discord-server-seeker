import requests,time
from random import randint
from dhooks import Webhook
import threading
from colorama import Fore, Back, init
init()

version = open('version.txt','r')

print(f'''\n\n\n\n\n\n\n\n

░▒▓███████▓▒░░▒▓█▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░                    
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░                   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                   
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                   
░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░                    
                                                                                                        
                                                                                                        
                         ░▒▓███████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
                        ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                        ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                         ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
                               ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                               ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
                        ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 

version: {Back.GREEN + version.readline() + Back.RESET}\n\n\n''')

version.close()

def createPayload(method: str, url: str, data = None):
    payload = { 'api_key': 'd64cd41c3eb3a716928ec5037f9b69cc', 'url': url } 
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
    for i in range(randint(4,8)):
        url += abc[randint(0,lenght)]
    return url
    
hook = Webhook('https://discord.com/api/webhooks/1201086934462763038/dwin_1dGa0ugJtlc65n0yucOTHaPCqlU-1yTwWXKERH2SI8tKslC5L0sC86Kci9czm1f')

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
