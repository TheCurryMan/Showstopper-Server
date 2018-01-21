from flask import Flask
from flask import request
from firebase import firebase
import urllib.request
import json
import findhottest
import geosnapshot

DEBUG = True
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://showstoppercruz.firebaseio.com', None)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/findhottest')
def hottest():
    return json.dumps(findhottest.find_pic(findhottest.get()))

@app.route('/geo', methods = ['GET'])
def geo():
    id = request.args.get('id')
    return json.dumps(geosnapshot.get(id))