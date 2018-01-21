from colordetect import clothes_color
from cnnclothes import predict
from PIL import Image
import pyrebase

#init firebase

items = ["top", "bot", "top", "top", "top", "sho", "top", "sho", "bot", "sho"] 
classes = ["t-shirt", "trouser", "pullover", "dress", "coat", "sandal", "shirt", "sneaker", "pants", "high-top"]

userId = '46Hv3U0JRiZPVfaDPxHlyF4PX5g1'
itemId = 'jewishoven'
description = 'very moist'

config = {
    "apiKey": "AIzaSyC99vx1nebCVnwmF4AhC1iAtBrKo-JpRSM",
    "authDomain": "showstoppercruz.firebaseapp.com",
    "databaseURL": "https://showstoppercruz.firebaseio.com",
    "storageBucket": "showstoppercruz.appspot.com"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
db = firebase.database()
storage.child(userId + "/" + itemId + ".jpeg").download("test.jpeg")
img = Image.open('test.jpeg')

#retrieve type
cat = items[predict(img)]

img1 = Image.open('test.jpeg')
#retrieve color
color = clothes_color("/Users/ashwinnathan/test.jpeg")

#retrieve class
tag = classes[predict(img1)]
print(cat)
print(color)
print(tag)


subcloset = db.child("users").child(userId).child("closet").child(cat).get()
newar = []
if subcloset is None:
	print('mike hunt')
	newar = [itemId]
else:
	newar = subcloset.val()
	newar.append(itemId);

print(newar)
db.child("users").child(userId).child("closet").child(cat).set(newar)



item = {'cat': cat, 'color': color, 'tag': tag, 'description': description}

db.child("items").child(itemId).set(item)
