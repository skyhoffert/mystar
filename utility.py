__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

def does_user_exist(username, password):
    f = open('users', 'r')
    
    for line in f.readlines():
        tokens = line.split(',', 1)
        if username == tokens[0]:
            if password == tokens[1].rstrip():
                return 'Success!'
            else:
                return 'Incorrect password.'
    
    return 'User not found.'