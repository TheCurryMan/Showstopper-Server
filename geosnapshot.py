from firebase import firebase
from geopy.distance import vincenty
from datetime import date
import json
firebase = firebase.FirebaseApplication('https://showstoppercruz.firebaseio.com/', None)

def get_map(id):
    print('Calculating...')
    result = firebase.get('/users', None)
    # print(result)
    mylat = '/users/' + id + '/lat'
    mylng = '/users/' + id + '/long'
    mycoords = [firebase.get(mylat, None), firebase.get(mylng, None)]
    coords = dict()
    for user in result.keys():
        if user != id:
            # print(user)
            lat = '/users/' + user + '/lat'
            lng = '/users/' + user + '/long'
            coords[user] = [firebase.get(lat, None), firebase.get(lng, None)]
    # result = firebase.get('/mUsers', None)
    map_coords = dict()
    for person in coords.keys():
        a = (coords[person][0], coords[person][1])
        b = (mycoords[0], mycoords[1])
        x = vincenty(a, b).meters
        if x < 10:
            map_coords[person] = a
    return map_coords

def nearby_outfits(id):
    peeps = get_map(id)
    today = str(date.today().year) + "-" + str(date.today().month) + "-" + str(date.today().day)
    clothing = {'top': [], 'bot': [], 'sho': []}
    # print(peeps.keys())
    for user in peeps.keys():
        link = '/users/' + user + '/outfits/' + today
        # print(link)
        # link2 = "/users/46Hv3U0JRiZPVfaDPxHlyF4PX5g1/outfits/2018-1-21"
        # print(link2)
        today_outfit = firebase.get(link, None)
        # print(today_outfit)
        clothing['top'].append(today_outfit['topID'])
        clothing['bot'].append(today_outfit['botID'])
        clothing['sho'].append(today_outfit['shoID'])
    print('Uploading...')

    url = '/users/' + id + '/searches'
    cur_top = (firebase.get(url + '/top', None))
    # print(type(cur_top))
    if cur_top is None:
        com_top = clothing['top']
    else:
        com_top = clothing['top']
        com_top = com_top + cur_top
    cur_bot = (firebase.get(url + '/bot', None))
    if cur_bot is None:
        com_bot = clothing['bot']
    else:
        com_bot = clothing['bot']
        com_bot = com_bot + cur_bot
    cur_sho = (firebase.get(url + '/sho', None))
    if cur_sho is None:
        com_sho = clothing['sho']
    else:
        com_sho = clothing['sho']
        com_sho = com_sho + cur_sho

    res_top = firebase.put('', url + '/top', com_top)
    res_bot = firebase.put('', url + '/bot', com_bot)
    res_sho = firebase.put('', url + '/sho', com_sho)
    print('Complete')
    fin = dict()
    fin['top_list'] = res_top
    fin['bot_list'] = res_bot
    fin['sho_list'] = res_sho
    return fin

# print(nearby_outfits('46Hv3U0JRiZPVfaDPxHlyF4PX5g1'))


