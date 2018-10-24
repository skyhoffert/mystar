__author__ = 'Sky Hoffert'
__copyright__ = 'Copyright 2018, Sky Hoffert'
__credits__ = ['Sky Hoffert']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Sky Hoffert'
__email__ = 'skyhoffert@gmail.com'
__status__ = 'Development'

from copy import deepcopy
from constants import *
import datetime
import json
from math import *
import numpy as np

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
    
    star['type'] = s
    star['mass'] = generate_star_mass(s)
    star['radius'] = generate_star_radius(s, star['mass'])
    star['surface_temp'] = generate_star_temperature(s, star['mass'], star['radius'])
    star['parent'] = ''
    star['colors'] = generate_star_colors(star)
    star['alternate_names'] = []

    return star

def generate_planet_details(p, system):
    '''
    Generates a dictionary object that fully describes a new planet
        @arg p: string; describes the type of planet
        @arg system: dict; describes the entire system
        @return: dict; all details about the new planet
    '''
    planet = {}

    # name is set first to a ? to indicate it is being modified
    planet['name'] = '?'

    planet['type'] = p
    planet['parent'] = system['stars'][np.random.randint(0,len(system['stars']))]['name']
    
    # now that the planet has a parent, it can be named properly
    planet['name'] = generate_planet_name(system, planet['parent'])

    planet['mass'] = generate_planet_mass(p)
    planet['radius'] = generate_planet_radius(p, planet['mass'])
    planet['semi_major_axis'] = generate_planet_sma(planet, system)
    planet['eccentricity'] = generate_planet_eccentricity(planet, system)
    planet['inclination'] = generate_planet_inclination(planet, system)
    planet['rotation_period'] = generate_planet_rotation_period(planet)
    planet['axial_tilt'] = generate_planet_axial_tilt(planet)
    planet['albedo'] = generate_planet_albedo(planet)
    planet['surface_pressure'] = generate_planet_surface_pressure(planet)
    planet['surface_temp_min'] = generate_planet_temp_min(planet)
    planet['surface_temp_max'] = generate_planet_temp_max(planet)
    planet['colors'] = generate_planet_colors(planet)

    planet['rings'] = []
    planet['moons'] = []
    planet['alternate_names'] = []
    
    # Moons:
    avg = PLANET_AVERAGE_NUM_MOONS[p]
    # use a normal curve with mean equal to average and a fitting stddev
    num_moons = abs(floor(np.random.normal(avg,avg/2)))
    # special case, if gas giant, add minimum number of moons!
    if p == 'Gas Giant':
        num_moons += PLANET_AVERAGE_NUM_MOONS[p]
    
    # Rings:
    # only applies to gas giants!
    if p == 'Gas Giant':
        # TODO: add chance for rings to gas giants
        pass
    
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

    # use the difference in mass to calculate a correlated difference in radius
    num_stddevs_away = (mass - STAR_AVERAGE_MASSES[s]) / STAR_STDDEV_MASSES[s]
    radius = STAR_AVERAGE_RADII[s]  + STAR_STDDEV_RADII[s] * num_stddevs_away * np.random.normal(1,0.1)

    return round(radius)

def generate_star_temperature(s, mass, radius):
    '''
    Generate the temperature of a given type of Star, depending on Mass and Radius
        @arg s: string; the type of Star provided
        @arg mass: int; mass of the given Star in kg
        @arg radius: int; radius of the given Star in m
        @return: int; temperature of given star in Kelvin
    '''

    num_stddevs_away = (mass - STAR_AVERAGE_MASSES[s]) / STAR_STDDEV_MASSES[s]
    temp = STAR_AVERAGE_TEMPERATURE[s] + STAR_STDDEV_TEMPERATURE[s] * num_stddevs_away * np.random.normal(1,0.1)

    return round(temp)

def generate_star_colors(star):
    '''
    Generates colors of a Star, given the type
        @arg star: dict; describes the Star
        @return: list; of colors describing the Star
    '''

    # fetch the predefined possible colors
    temp = STAR_COLORS[star['type']]
    
    # remove wrong colors if giant type
    if star['type'] in ['Main Sequence High Mass', 'Giant', 'Supergiant', 'Hypergiant']:
        del temp[round(np.random.uniform(0.0, 1.0))]

    return temp

# ===================================================================================================
# ======================================== Planet Generation ========================================
# ===================================================================================================
def generate_planet_mass(p):
    '''
    Generates a planet mass, given the type of planet
        @arg p: string; indicates the type of planet
        @return: int; value for mass of given planet
    '''

    # first, find the average mass for given type of star
    mean = PLANET_AVERAGE_MASSES[p]
    stddev = PLANET_STDDEV_MASSES[p]

    # use a normal curve to generate Star details
    mass = np.random.normal(mean, stddev)
    return round(mass,-int(log10(mass)-3))

def generate_planet_radius(p, mass):
    '''
    Generates a planet radius, given the type of planet and mass
        @arg p: string; indicates the type of planet
        @arg mass: int; mass of the given planet in kg
        @return: int; value for radius of given planet
    '''

    # use the difference in mass to calculate a correlated difference in radius
    num_stddevs_away = (mass - PLANET_AVERAGE_MASSES[p]) / PLANET_STDDEV_MASSES[p]
    radius = PLANET_AVERAGE_RADII[p]  + PLANET_STDDEV_RADII[p] * num_stddevs_away * np.random.normal(1,0.1)

    return round(radius)

def generate_planet_sma(planet, system):
    '''
    Generates a planet orbital radius (semi-major-axis), given the planet and system
        @arg planet: dict; describes the given planet
        @arg system: dict; describes the entire system
        @return: int; orbital radius value in meters
    '''

    # Loop until a good sma is found
    passing = False
    while not passing:
        planet['semi_major_axis'] = np.random.chisquare(5)*SEMI_MAJOR_AXIS_FACTOR + SEMI_MAJOR_AXIS_OFFSET
        sma = planet['semi_major_axis']
        passing = True
        for p in system['planets']:
            if planet['parent'] == p['parent']:
                this_clearance = calculate_orbital_clearing(planet, system)
                p_clearance = calculate_orbital_clearing(p, system)
                max_sma = p['semi_major_axis'] - p_clearance - this_clearance
                min_sma = p['semi_major_axis'] + p_clearance + this_clearance
                if sma > max_sma and sma < min_sma:
                    passing = False
                    break

    return round(sma)

def generate_planet_name(system, parent):
    '''
    Generates a planet name given the system and parent
        @arg system: dict; describes the entire system
        @arg parent: dict; describes the parent object
        @return: string; name for the planet
    '''

    # keep track of how many children the parent has
    num_parent_children = 0

    # loop through all planets in the system
    for planet in system['planets']:
        # detect if this planet is the one we are naming
        if planet['name'] == '?':
            continue

        # otherwise, check if the parent has other children
        if planet['parent'] == parent:
            num_parent_children += 1

    # add a lowercase letter to indicate a planet
    return '{}{}'.format(parent, chr(ord('a') + num_parent_children))

def generate_planet_eccentricity(planet, system):
    '''
    Generates an eccentricity value based on the existing system
        @arg planet: dict; describes the target planet
        @arg system: dict; describes the target system
        @return: float; eccentricity value for planetary orbit
    '''

    # first, find the average mass for given type of star
    mean = PLANET_AVERAGE_ECCENTRICITY[planet['type']]
    stddev = PLANET_STDDEV_ECCENTRICITY[planet['type']]

    # use a normal curve to generate Star details
    ecc = abs(np.random.normal(mean, stddev))
    return round(ecc,6)

def generate_planet_inclination(planet, system):
    '''
    Generates an inclination for this planet, based off the existing system
        @arg planet: dict; describes the target planet
        @arg system: dict; describes the target system
        @return: float; inclination angle in degrees
    '''

    # if the first planet, return 0 degrees - our systems will use the first planet as a basis
    if planet['name'][-1] == 'a':
        return 0.0

    i = abs(np.random.normal(PLANET_AVERAGE_INCLINATION, PLANET_STDDEV_INCLINATION))

    return round(i, 4)

def generate_planet_rotation_period(planet):
    '''
    Generates a rotational period
        @arg planet: dict; describes the target planet
        @return: float; rotational period in seconds
    '''

    # first, find the average and stddev for each type
    mean = PLANET_AVERAGE_ROTATION_PERIOD[planet['type']]
    stddev = PLANET_STDDEV_ROTATION_PERIOD[planet['type']]

    rot_per = abs(np.random.normal(mean, stddev))

    # make some planets randomly have retrograde rotation, not gas giants though
    if planet['type'] == 'Dwarf' or planet['type'] == 'Gas Giant':
        if np.random.uniform(0.0, 1.0) < PLANET_RETROGRADE_CHANCE:
            # retrograde rotations probably have longer rotation rates as well
            rot_per *= -PLANET_RETROGRADE_LENGTH_INCREASE

    return round(rot_per)

def generate_planet_axial_tilt(planet):
    '''
    Generates an axial tilt for the given planet
        @arg planet: dict; describes the target planet
        @return: float; axial tilt in degrees (always positive)
    '''

    mean = PLANET_AVERAGE_AXIAL_TILT[planet['type']]
    stddev = PLANET_STDDEV_AXIAL_TILT[planet['type']]

    tilt = abs(np.random.normal(mean, stddev))
    return round(tilt)
    
def generate_planet_albedo(planet):
    '''
    Generates an albedo (reflectiveness) for the given planet
        @arg planet: dict; describes the target planet
        @return: float; albedo
    '''

    mean = PLANET_AVERAGE_ALBEDO[planet['type']]
    stddev = PLANET_STDDEV_ALBEDO[planet['type']]

    a = abs(np.random.normal(mean, stddev))
    return round(a, 3)

def generate_planet_surface_pressure(planet):
    '''
    TODO
    '''

    # TODO
    P = 101.325

    return round(P, 4)
    
def generate_planet_temp_min(planet):
    '''
    TODO
    '''

    # TODO
    T = 184

    return round(T, 4)
    
def generate_planet_temp_max(planet):
    '''
    TODO
    '''

    # TODO
    T = 330

    return round(T, 4)
    
def generate_planet_colors(planet):
    '''
    Generates a list of colors to associate with the given planet
        @arg planet: dict; describes the planet
        @return: list; colors that should be attached to the planet
    '''

    colors = []

    # make a deep copy, not to interfere with the real array
    temp = deepcopy(PLANET_ALL_COLORS)

    # shuffle the copy we made to randomize
    np.random.shuffle(temp)

    # randomly (uniformly) select a number of colors
    num = np.random.randint(PLANET_MIN_COLORS, PLANET_MAX_COLORS)

    # iterate through as many as was chosen
    for i in range(0, num):
        colors.append(temp[0])
        del temp[0]

    return colors

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

    return int(np.random.uniform(0.0, 1.0) * longest)

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
    system_name  = str(1000 + np.random.randint(0, 9000))
    # second element is a two part letter definition using the greek alphabet
    system_name += ' ' + SYSTEM_NAMES[1][np.random.randint(0, len(SYSTEM_NAMES[1]))]
    system_name += '-' + SYSTEM_NAMES[1][np.random.randint(0, len(SYSTEM_NAMES[1]))]
    # third element is a constellation
    system_name += ' ' + SYSTEM_NAMES[0][np.random.randint(0, len(SYSTEM_NAMES[0]))]

    return system_name

# ===================================================================================================
# ============================================ Utility ==============================================
# ===================================================================================================
def find_parent_star(planet, system):
    '''
    Returns the dict describing the parent star of a given planet in a given system
        @arg planet: dict; describes the target planet
        @arg system: dict; describes the target star
        @return: dict; describing the parent star
    '''

    # search the system for the parent
    for star in system['stars']:
        if planet['parent'] == star['name']:
            return star
    
    # if no parent is found, return None
    return None

def calculate_orbital_clearing(planet, system):
    '''
    Calculates orbital clearing given certain planet parameters
        @arg planet: dict; describes the target planet
        @arg system: dict; describes the target system
        @return: float; orbital clearing distance in m
    '''

    a = planet['semi_major_axis']
    m = planet['mass']
    M = find_parent_star(planet, system)['mass']

    r_soi = a * (m / M)**(2/5)
    clearing = r_soi * ORBIT_CLEAR_FACTOR

    if clearing < ORBIT_CLEAR_INCREASE_LIMIT:
        clearing *= ORBIT_CLEAR_INCREASE_FACTOR

    return clearing

# ===================================================================================================
# ============================================ Main =================================================
# ===================================================================================================
def main():
    '''
    Main function for the generate_system program
    '''

    # First, we should seed the random generator! This way we can get consistent results
    np.random.seed(0)

    system_name = generate_system_name()
    print('System: {}'.format(system_name))

    num_stars = generate_value_from_list(NUM_STARS)
    stars = []
    star_types = []
    print('================================ {} Star(s) =================================='.format(str(num_stars)))
    star_letter_int = ord('A')
    for star in range(0, num_stars):
        star_type = generate_value_from_list(STAR_TYPES)
        details = generate_star_details(star_type)
        name = '{} {}'.format(system_name, chr(star_letter_int))
        details['name'] = name
        print(name)
        print('  ', details)
        star_letter_int += 1
        star_types.append(star_type)
        stars.append(details)

    # at this point we can perform some calculations for system values
    age = generate_system_age(star_types)

    # assemble values in to a dictionary
    system_dict = {"discovered_by": "sky", "date_discovered": "{0:%d %b %Y}".format(datetime.datetime.utcnow()), "name": system_name,    "age": age, "stars": stars, "planets": []}
    
    # now, time to generate a random number of planets
    num_planets = generate_value_from_list(NUM_PLANETS)
    planets = []
    print('================================ {} Planets ================================'.format(num_planets))
    for p in range(0, num_planets):
        planet = generate_value_from_list(PLANET_TYPES)
        details = generate_planet_details(planet, system_dict)
        planets.append(details)
        system_dict['planets'].append(details)

    # DEBUG
    print(json.dumps(system_dict, sort_keys=True, indent=2))
    
if __name__ == '__main__':
    main()