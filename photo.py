from colordetect import clothes_color
from cnnclothes import predict
from PIL import Image
import pyrebase
from PIL import Image
import requests
from io import BytesIO


#init firebase

items = ["top", "bot", "top", "top", "top", "sho", "top", "sho", "bot", "sho"] 
classes = ["t-shirt", "trouser", "pullover", "dress", "coat", "sandal", "shirt", "sneaker", "pants", "high-top"]

def outputs(userId, itemId):	

	description = 'very moist'

	config = {
	    "apiKey": "AIzaSyC99vx1nebCVnwmF4AhC1iAtBrKo-JpRSM",
	    "authDomain": "showstoppercruz.firebaseapp.com",
	    "databaseURL": "https://showstoppercruz.firebaseio.com",
	    "storageBucket": "showstoppercruz.appspot.com"
	}

	firebase = pyrebase.initialize_app(config)

	file_name = "test.jpeg"
	storage = firebase.storage()
	db = firebase.database()
	url = storage.child(userId + "/" + itemId + ".jpeg").get_url()
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))

	#retrieve type
	cat = items[predict(img)]

	#retrieve color
	color = clothes_color(url)

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
