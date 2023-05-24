import requests
import random

long_url = 55 # .onionのドメインは56文字で最後はd
w = 0
canconnect = 0
my_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
url=[]

while True:
    for i in range(long_url):
        url.append(my_list[random.randint(0,int(len(my_list)-1))])
    url = ''.join(url)
    url +="d"
    url= f"http://{url}.onion/"
    try:
        response = requests.get(url,proxies=dict(http='socks5h://127.0.0.1:9050', https='socks5h://127.0.0.1:9050'))
        if response.status_code == 200:
            w+=1
            canconnect+=1
            print(url,end=" ")
            print(f"Can connect \n ({canconnect}/{w})")
            print(url)
            with open("onion_site.txt", "a") as f:
                f.write(url)
        else:
            w+=1
            print(f"Not connect ({canconnect}/{w})")
    except:
        w+=1
        print(f"{url} \n Can't connect ({canconnect}/{w})")
    url=[]  # urlをリセットする
