from firebase import firebase
from collections import Counter
import requests
import json
from bs4 import BeautifulSoup

url = "http://www.hm.com/us/products/search?q="

firebase = firebase.FirebaseApplication('https://showstoppercruz.firebaseio.com/', None)

def get():
    result = firebase.get('/items', None)
    top = []
    bot = []
    sho = []
    for clothes in result.keys():
        if result[clothes]['cat'] == 'top':
                if result[clothes]['tag'] is not None and result[clothes]['color'] is not None:
                    art = result[clothes]['color'] + " " + result[clothes]['tag']
                    top.append(art)
        if result[clothes]['cat'] == 'bot':
                if result[clothes]['tag'] is not None and result[clothes]['color'] is not None:
                    art = result[clothes]['color'] + " " + result[clothes]['tag']
                    bot.append(art)
        if result[clothes]['cat'] == 'sho':
                if result[clothes]['tag'] is not None and result[clothes]['color'] is not None:
                    art = result[clothes]['color'] + " " + result[clothes]['tag']
                    sho.append(art)
    hot_top = get_most_common(top)
    hot_bot = get_most_common(bot)
    hot_sho = get_most_common(sho)
    hot_list = [hot_top, hot_bot, hot_sho]

    split = []
    ids = dict()
    urls = dict()
    fin = dict()
    split = split + hot_list[0].split() + hot_list[1].split() + hot_list[2].split()
    result = firebase.get('/items', None)
    found_top = False
    found_bot = False
    found_sho = False
    for clothes in result.keys():
        if result[clothes]['cat'] == 'top':
             if result[clothes]['color'] == split[0] and result[clothes]['tag'] == split[1] and found_top == False:
                ids['top'] = clothes
                found_top = True
        if result[clothes]['cat'] == 'bot':
             if result[clothes]['color'] == split[2] and result[clothes]['tag'] == split[3] and found_bot == False:
                ids['bot'] = clothes
                found_bot = True
        if result[clothes]['cat'] == 'sho':
             if result[clothes]['color'] == split[4] and result[clothes]['tag'] == split[5] and found_sho == False:
                ids['sho'] = clothes
                found_sho = True
    url1 = url + hot_list[0].replace(" ", "%20")
    url2 = url + hot_list[1].replace(" ", "%20")
    url3 = url + hot_list[2].replace(" ", "%20")
    urls['url1'] = url1
    urls['url2'] = url2
    urls['url3'] = url3
    fin['clothing_id'] = ids
    fin['clothing_url'] = urls

    return fin

def get_most_common(color_list):
    order = Counter(color_list)
    x = (list(order.keys())[0])
    return x


# print(get())