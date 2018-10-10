__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

from copy import deepcopy
from math import floor
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

# ======== Constants ========
NUM_STARS = [(1,10), (2,9), (3,3), (4,1)]
NUM_PLANETS = [(4,10), (5,10), (6,10), (7,9), (8,9), (9,9), (10,8), (11,8), (12,8), (13,7), (14,7), (15,6)]
STAR_TYPES = [('Brown Dwarf Star',2), ('Red Dwarf Star', 20), ('Main Sequence Average Mass Star', 8), ('Main Sequence High Mass Star', 8), ('Giant Star', 4), ('Supergiant Star', 3), ('Hypergiant Star', 2), ('Neutron Star', 1)]
PLANET_TYPES = [('Gas Giant Planet', 4), ('Terrestrial Planet', 4), ('Dwarf Planet', 5)]

# ======== Functions ========
def generate_value_from_list(list):
    # first, calculate the total value of all weights
    total_dist = 0
    for l in list:
        total_dist += l[1]
    
    # generate a random value
    val = np.random.uniform(0,1) * total_dist
    total_running = 0
    
    # now, find which type based on that random value
    for l in list:
        total_running += l[1]
        if val < total_running:
            return l[0]

def system_type(num_stars):
    if num_stars == 1:
        return 'Single Star'
    elif num_stars == 2:
        return 'Binary Star System'
    elif num_stars == 3:
        return 'Triple Star System'
    elif num_stars == 4:
        return 'Double-Double Star System'
    
# ======== Main =============
def main():
    print('======== Stars ========')
    num_stars = generate_value_from_list(NUM_STARS)
    print('Number of Stars: ', num_stars)
    for star in range(0, num_stars):
        print(generate_value_from_list(STAR_TYPES))
    
    print('======== Planets ========')
    num_planets = generate_value_from_list(NUM_PLANETS)
    print('Number of Planets: ', num_planets)
    for planet in range(0, num_planets):
        print(generate_value_from_list(PLANET_TYPES))
    
    '''
    fig,ax = plt.subplots()
    ax.hist(num_stars)
    plt.show()
    '''
    
if __name__ == '__main__':
    main()