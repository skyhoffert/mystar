__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

import json
from flask import Flask, request
import pickle
from utility import *

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return 'Index!'

@app.route('/stars', methods=['GET'])
def stars():
    return 'Stars!'
    
@app.route('/verify', methods=['POST'])
def verify():
    payload = request.json
    
    did_auth = does_user_exist(payload['username'], payload['password'])
    if did_auth != 'Success!':
        return did_auth
    
    return 'Successfully authenticated!'
    
@app.route('/add_user', methods=['POST'])
def add_user():
    payload = request.json
    
    if payload['username'] != 'admin':
        return 'Elevated priveliges required to add new user.'
    
    did_auth = does_user_exist(payload['username'], payload['password'])
    if did_auth != 'Success!':
        return did_auth
    
    did_add = add_new_user(payload['new_user']['username'], payload['new_user']['password'])
    if did_add != 'Success!':
        return did_add
    
    return 'Successfully added new user!'
    
if __name__ == '__main__':
    app.run()