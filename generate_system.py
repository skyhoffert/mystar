__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

import datetime
from copy import deepcopy
import json
from math import *
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

# ================================ Constants ================================
NUM_STARS = ((1,10), (2,9), (3,3), (4,1))
NUM_PLANETS = ((4,10), (5,10), (6,10), (7,9), (8,9), (9,9), (10,8), (11,8), (12,8), (13,7), (14,7), (15,6))
STAR_TYPES = (('Brown Dwarf',2), ('Red Dwarf', 20), ('Main Sequence Average Mass', 8), \
('Main Sequence High Mass', 8), ('Giant', 4), ('Supergiant', 3), ('Hypergiant', 2), ('Neutron', 1))
PLANET_TYPES = (('Gas Giant', 4), ('Terrestrial', 4), ('Dwarf', 5))
SYSTEM_NAMES = (('Andromeda', 'Aquarius', 'Aquila', 'Ara', 'Argo', 'Aries', 'Auriga', 'Bootes', 'Cancer', 'Canis', \
'Capricornus', 'Cassiopeia', 'Centaurus', 'Cepheus', 'Cetus', 'Corona', 'Corvus', 'Crater', 'Cygnus', 'Delphinus', \
'Draco', 'Equuleus', 'Eridanus', 'Gemini', 'Hercules', 'Hydra', 'Leo', 'Lepus', 'Libra', 'Lupus', 'Lyra', 'Ophiuchus',\
 'Orion', 'Pegasus', 'Perseus', 'Pisces', 'Sagittarius', 'Scorpius', 'Serpens', 'Taurus', 'Triangulum', 'Ursa', 'Virgo'), \
('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', \
'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega'))

PLANET_AVERAGE_MASSES = {'Gas Giant':1e26, 'Terrestrial':5e23, 'Dwarf':1e21}
PLANET_AVERAGE_NUM_MOONS = {'Gas Giant':20, 'Terrestrial':2, 'Dwarf': 0.78}

# ================================ Functions ================================
def generate_value_from_list(list):
    '''
    Returns a value from a predefined list meeting the proper format
        @arg list: list; holds values that match the format (value, weight)
        @return: variable; the "random" value generated
    '''
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

def generate_star_details(s):
    '''
    Generates a dictionary object that fully describes a new Star
        @arg s: string; describes the type of Star
        @return: dict; all details about the new Star
    '''

    star = {}

    # Mass:
    star['mass'] = generate_star_mass(s)

    # Radius:
    # TODO
    
    # Temperature
    # TODO

    return star

def generate_planet_details(p):
    '''
    Generates a dictionary object that fully describes a new planet
        @arg p: string; describes the type of planet
        @return: dict; all details about the new planet
    '''
    planet = {}

    # Mass:
    # create a random exponent using a normal curve with (mean, stddev)
    exponent = np.random.normal(0,0.6)
    # use that exponent as a power of 10 to keep mass close to relative average
    planet['mass'] = PLANET_AVERAGE_MASSES[p] * pow(10,exponent)
    
    # Moons:
    avg = PLANET_AVERAGE_NUM_MOONS[p]
    # use a normal curve with mean equal to average and a fitting stddev
    planet['nummoons'] = abs(floor(np.random.normal(avg,avg/2)))
    # special case, if gas giant, add minimum number of moons!
    if p == 'Gas Giant':
        planet['nummoons'] += PLANET_AVERAGE_NUM_MOONS[p]
    
    # Rings:
    # only applies to gas giants!
    if p == 'Gas Giant':
        # use a 50/50 chance for now ;)
        planet['rings'] = [True] if random.random() < 0.5 else []
    
    return planet

def generate_star_mass(s):
    '''
    Generates a star mass, given the type of Star
        @arg s: string; indicates the type of star
        @return: int; value for mass of given star
    '''

    # first, find the average mass for given type of star
    mean = 0
    stddev = 0

    # unfortunately, this must be done manually
    if s == 'Brown Dwarf':
        mean = 8.75e28
        stddev = 1.5e28
    elif s == 'Red Dwarf':
        mean = 5.72e29
        stddev = 1.5e29
    elif s == 'Main Sequence Average Mass':
        mean = 1.00e30
        stddev = 1.2e29
    elif s == 'Main Sequence High Mass':
        mean = 5.00e30
        stddev = 0.8e30
    elif s == 'Giant':
        mean = 1.00e31
        stddev = 1.2e30
    elif s == 'Supergiant':
        mean = 7.96e31
        stddev = 1.5e31
    elif s == 'Hypergiant':
        mean = 2.50e32
        stddev = 2.0e31

    # use a normal curve to generate Star details
    mass = np.random.normal(mean, stddev)
    return round(mass,-int(log10(mass)-3))

def generate_star_radius(s, mass):
    '''
    Generates the radius of a given type of Star, depending on the Mass
        @arg s: string; the type of Star provided
        @arg mass: int; mass of the given Star in kg to correlate a radius to
        @return: int; radius of given Star in meters
    '''

    # TODO

    return 6371e3

def generate_system_age(stars):
    '''
    Generates a system age, given Stars present in the system
        @arg stars: list; provides given stars in a system
        @return: int; age of the Star in years
    '''

    # use this variable to keep track of the limiting star in the system
    # Star cannot be older than the age of the Universe...
    longest = 13.7e9

    # check every Star given
    for s in stars:
        if s == 'Main Sequence Average Mass':
            # Stars like the sun last up to around 10 billion years
            longest = 10e9 if 10e9 < longest else longest
        elif s == 'Main Sequence High Mass':
            # Higher mass Stars than the Sun last less time
            longest = 5e9 if 5e9 < longest else longest
        elif s == 'Giant':
            longest = 1e9 if 1e9 < longest else longest
        elif s == 'Supergiant':
            longest = 100e6 if 100e6 < longest else longest
        elif s == 'Hypergiant':
            # Hypergiants have a very short lifetime
            longest = 10e6 if 10e6 < longest else longest

    return int(random.random() * longest)

def system_type(num_stars):
    '''
    Return a string as indication of the system type
        @arg num_stars: int; indicates the number of stars in a given system
        @return: string; a description of the given system
    '''
    if num_stars == 1:
        return 'Single Star'
    elif num_stars == 2:
        return 'Binary Star System'
    elif num_stars == 3:
        return 'Triple Star System'
    elif num_stars == 4:
        return 'Double-Double Star System'

def generate_system_name():
    '''
    Generates a new, random system name!
        @return: string; name of a new system
    '''
    # first element is a random, 4 digit number
    system_name  = str(1000 + random.randint(0, 8999))
    # second element is a two part letter definition using the greek alphabet
    system_name += ' ' + SYSTEM_NAMES[1][random.randint(0, len(SYSTEM_NAMES[1])-1)]
    system_name += '-' + SYSTEM_NAMES[1][random.randint(0, len(SYSTEM_NAMES[1])-1)]
    # third element is a constellation
    system_name += ' ' + SYSTEM_NAMES[0][random.randint(0, len(SYSTEM_NAMES[0])-1)]

    return system_name

def main():
    '''
    Main function for the generate_system program
    '''
    system_name = generate_system_name()
    print(system_name)

    num_stars = generate_value_from_list(NUM_STARS)
    stars = []
    print('================================ {} Star(s) =================================='.format(str(num_stars)))
    star_letter_int = ord('A')
    for star in range(0, num_stars):
        star_type = generate_value_from_list(STAR_TYPES)
        print('{} {}: {}'.format(system_name, chr(star_letter_int), star_type))
        details = generate_star_details(star_type)
        name = '{} {}'.format(system_name, chr(star_letter_int))
        details['name'] = name
        print('  ', details)
        star_letter_int += 1
        stars.append(star_type)
    
    num_planets = generate_value_from_list(NUM_PLANETS)
    planets = []
    print('================================ {} Planets ================================'.format(num_planets))
    for p in range(0, num_planets):
        planet = generate_value_from_list(PLANET_TYPES)
        print(planet)
        details = generate_planet_details(planet)
        print('  ', details)
        planets.append(details)
    
    # finally, perform some calculations for system values
    age = generate_system_age(stars)

    # assemble values in to a dictionary
    system_dict = {"discovered_by": "sky", "date_discovered": "{0:%d %b %Y}".format(datetime.datetime.utcnow()), "name": system_name, \
    "age": age, "stars": [], "planets": []}

    # DEBUG
    print(system_dict)
    
if __name__ == '__main__':
    main()