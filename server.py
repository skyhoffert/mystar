__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return 'Index.'

@app.route('/stars', methods=['GET'])
def stars():
    return 'Stars.'
    
if __name__ == '__main__':
    app.run()