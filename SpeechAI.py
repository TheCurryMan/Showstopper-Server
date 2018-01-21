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


if __name__ == '__main__':
    app.run()



