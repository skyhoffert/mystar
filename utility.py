__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

import sys

def does_user_exist(username, password):
    f = open('users.log', 'r')
    
    for line in f.readlines():
        tokens = line.split(',', 1)
        if username == tokens[0]:
            if password == tokens[1].rstrip():
                return 'Success!'
            else:
                return 'Incorrect password.'
    
    return 'User not found.'
    
def add_new_user(username, password):
    f_in = open('users.log', 'r')
    lines = []
    
    for line in f_in.readlines():
        tokens = line.split(',', 1)
        if username != tokens[0]:
            lines.append(line)
            
    f_in.close()
    
    f_out = open('users.log', 'w')
    
    for line in lines:
        f_out.write(line)
    
    f_out.write(username)
    f_out.write(',')
    f_out.write(password)
    f_out.write('\n')
    
    return 'Success!'
    
def get_user_system(username):
    try:
        f = open('systems/{}.starsystem'.format(username), 'r')
    except:
        return False
    full = ''
    
    for line in f.readlines():
        full += line
    
    return full
    



