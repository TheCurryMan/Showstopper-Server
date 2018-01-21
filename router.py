from flask import Flask
from flask import request
from firebase import firebase
import json
import findhottest
import geosnapshot
import photo


DEBUG = True
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://showstoppercruz.firebaseio.com', None)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/findhottest')
def hottest():
    return json.dumps(findhottest.get())

@app.route('/geo', methods = ['GET'])
def geo():
    user = request.args.get('id')
    return json.dumps(geosnapshot.get_map(user))

@app.route('/outfits', methods = ['GET'])
def outfits():
    ids = request.args.get('id')
    return json.dumps(geosnapshot.nearby_outfits(ids))

@app.route('/store', methods = ['GET'])
def store():
    user_id = request.args.get('user_id')
    pic_id = request.args.get('pic_id')
    photo.outputs(user_id, pic_id)
    return "CONGRATS! ITS STORED U AIDS"


