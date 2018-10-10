__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

import json
import pickle
import requests
import sys

def preamble(num, descr):
    print('[TEST ] Beginning test', num, '-', descr)
    sys.stdout.flush()
    
def postamble(num):
    print('[TEST ] Test', num, 'was successful!')
    print()
    sys.stdout.flush()

def log(t):
    print('[ LOG ]', t)

def main():
    print()
    testnum = 0
    
    preamble(testnum, 'GET request on main page')
    resp = requests.get('http://localhost:5000/')
    log(resp.text)
    assert('!' in resp.text)
    postamble(testnum)
    testnum += 1
    
    preamble(testnum, 'Authentication for known user')
    payload = json.loads('{"username":"sky", "password":"earthisacoolplanet"}')
    resp = requests.post('http://localhost:5000/verify', json=payload)
    log(resp.text)
    assert('!' in resp.text)
    postamble(testnum)
    testnum += 1
    
    preamble(testnum, 'Authentication for incorrect username')
    payload = json.loads('{"username":"skyguy", "password":"earthisacoolplanet"}')
    resp = requests.post('http://localhost:5000/verify', json=payload)
    log(resp.text)
    assert('!' not in resp.text)
    postamble(testnum)
    testnum += 1
    
    preamble(testnum, 'Authentication for incorrect password')
    payload = json.loads('{"username":"sky", "password":"marsisacoolplanet"}')
    resp = requests.post('http://localhost:5000/verify', json=payload)
    log(resp.text)
    assert('!' not in resp.text)
    postamble(testnum)
    testnum += 1
    
    preamble(testnum, 'Attempt test that passwords with commas in them are okay')
    payload = json.loads('{"username":"sky2", "password":"password,withacommainit"}')
    resp = requests.post('http://localhost:5000/verify', json=payload)
    log(resp.text)
    assert('!' in resp.text)
    postamble(testnum)
    testnum += 1
    
    preamble(testnum, 'Attempt to add/modify an existing user')
    payload = json.loads('{"username":"admin", "password":"europa!m=5e22r=2e3y=1610", "new_user":{"username":"newsky","password":"NewSuperCoolPassword"}}')
    resp = requests.post('http://localhost:5000/add_user', json=payload)
    log(resp.text)
    assert('!' in resp.text)
    payload = json.loads('{"username":"newsky", "password":"NewSuperCoolPassword"}')
    resp = requests.post('http://localhost:5000/verify', json=payload)
    log(resp.text)
    assert('!' in resp.text)
    postamble(testnum)
    testnum += 1
    
    preamble(testnum, 'Pull down a known system')
    payload = json.loads('{"username":"sky", "type":"get"}')
    resp = requests.post('http://localhost:5000/system', json=payload)
    log(json.loads(resp.text))
    assert('!' in resp.text)
    postamble(testnum)
    testnum += 1
    
if __name__ == '__main__':
    main()