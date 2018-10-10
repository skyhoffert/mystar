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
PLANET_TYPES = [('Gas Giant', 4), ('Terrestrial', 4), ('Dwarf', 5)]

PLANET_AVERAGE_MASSES = {'Gas Giant':1e26, 'Terrestrial':5e23, 'Dwarf':1e21}
PLANET_AVERAGE_NUM_MOONS = {'Gas Giant':20, 'Terrestrial':2, 'Dwarf': 0.78}

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

def generate_planet_details(p):
    planet = {}
    exponent = np.random.normal(0,0.6)
    planet['mass'] = PLANET_AVERAGE_MASSES[p] * pow(10,exponent)
    
    avg = PLANET_AVERAGE_NUM_MOONS[p]
    planet['nummoons'] = abs(floor(np.random.normal(avg,avg/2)))
    if p == 'Gas Giant':
        planet['nummoons'] += PLANET_AVERAGE_NUM_MOONS[p]
    
    return planet 

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
    num_stars = generate_value_from_list(NUM_STARS)
    print('========',str(num_stars), 'Stars ========')
    for star in range(0, num_stars):
        print(generate_value_from_list(STAR_TYPES))
    
    num_planets = generate_value_from_list(NUM_PLANETS)
    print('========', num_planets,'Planets ========')
    for p in range(0, num_planets):
        planet = generate_value_from_list(PLANET_TYPES)
        print(planet)
        details = generate_planet_details(planet)
        print('  ', details)
    
if __name__ == '__main__':
    main()