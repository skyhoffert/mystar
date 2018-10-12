__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

from constants import *
import datetime
from math import *
import numpy as np
import random

# ===================================================================================================
# ============================================ Functions ============================================
# ===================================================================================================
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
    planet['mass'] = generate_planet_mass(p)
    
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

# ===================================================================================================
# ========================================== Star Generation ========================================
# ===================================================================================================
def generate_star_mass(s):
    '''
    Generates a star mass, given the type of Star
        @arg s: string; indicates the type of star
        @return: int; value for mass of given star
    '''

    # first, find the average mass for given type of star
    mean = STAR_AVERAGE_MASSES[s]
    stddev = STAR_STDDEV_MASSES[s]

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

# ===================================================================================================
# ======================================== Planet Generation ========================================
# ===================================================================================================
def generate_planet_mass(p):
    '''
    Generates a planet mass, given the type of planet
        @arg s: string; indicates the type of planet
        @return: int; value for mass of given planet
    '''

    # load the mass and stddev from the constants file
    mean = PLANET_AVERAGE_MASSES[p]
    stddev = PLANET_STDDEV_MASSES[p]

    # use a normal curve to generate Star details
    power = np.random.normal(0, stddev)
    mass = mean * pow(10, power)
    return round(mass,-int(log10(mass)-3))

# ===================================================================================================
# ======================================== System Generation ========================================
# ===================================================================================================
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
        longest = STAR_LIFETIMES[s] if STAR_LIFETIMES[s] < longest else longest

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

# ===================================================================================================
# ============================================ Main =================================================
# ===================================================================================================
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
    system_dict = {"discovered_by": "sky", "date_discovered": "{0:%d %b %Y}".format(datetime.datetime.utcnow()), "name": system_name,    "age": age, "stars": [], "planets": []}

    # DEBUG
    print(system_dict)
    
if __name__ == '__main__':
    main()