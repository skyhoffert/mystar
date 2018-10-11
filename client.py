__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

import json
import math
import pickle
import requests
import sys
import threading
import time
from tkinter import Tk, Canvas, PhotoImage

# ======== constants ================
WAIT_TIME = 0.01
IMG_WIDTH_START = 128
IMG_WIDTH_NEW = 256
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 720

# ======== utility functions ========
def log(t):
    print('[ LOG ]', t)
    sys.stdout.flush()
    
def move_image(canvas, image):
    for i in range(0,100):
        canvas.move(image, 1, 1)
        time.sleep(WAIT_TIME)

def main_state_thread():
    while True:
        # fetch sky's system from the server
        payload = pickle.dumps(json.loads('{"username":"sky", "type":"get"}'))
        resp = requests.post('http://localhost:5000/system', data=payload)
        json_obj = json.loads(resp.json())

# ======== main function ============
def main():
    root = Tk()
    root.title('mystar')
    
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    
    image_objects = []
    images = []
    
    # background image
    img = PhotoImage(file='gfx/black.png')
    img = img.zoom(math.ceil(CANVAS_WIDTH/IMG_WIDTH_START))
    image_objects.append(img)
    images.append(canvas.create_image(0, 0, image=img, anchor='nw'))
    
    # Sun image
    img = PhotoImage(file='gfx/sol.png')
    img = img.zoom(math.ceil(IMG_WIDTH_NEW / IMG_WIDTH_START))
    image_objects.append(img)
    images.append(canvas.create_image(-IMG_WIDTH_NEW*3/8, -IMG_WIDTH_NEW*3/8, image=img, anchor='nw'))
    
    # create threads
    moving_image_thread = threading.Thread(target=move_image, args=(canvas, images[1]))
    main_thread = threading.Thread(target=main_state_thread)
    
    # start threads
    #moving_image_thread.start()
    main_thread.start()
    
    # start the GUI
    root.mainloop()
    
    # join threads
    #moving_image_thread.join()
    main_thread.join()

if __name__ == '__main__':
    main()