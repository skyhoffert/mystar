# constants for mystar

NUM_STARS = ((1,10), (2,9), (3,3), (4,1))
NUM_PLANETS = ((4,10), (5,10), (6,10), (7,9), (8,9), (9,9), (10,8), (11,8), (12,8), (13,7), (14,7), (15,6))

STAR_TYPES = (('Brown Dwarf',2), ('Red Dwarf', 20), ('Main Sequence Average Mass', 8), ('Main Sequence High Mass', 8), ('Giant', 4), ('Supergiant', 3), ('Hypergiant', 2), ('Neutron', 1))
PLANET_TYPES = (('Gas Giant', 4), ('Terrestrial', 4), ('Dwarf', 5))

# options for possible System Names
# arbitrarily, I chose constellations and greek letters
# this may make names seem like they have meaning, but they really don't
SYSTEM_NAMES = (('Andromeda', 'Aquarius', 'Aquila', 'Ara', 'Argo', 'Aries', 'Auriga', 'Bootes', 'Cancer', 'Canis', 'Capricornus', 'Cassiopeia', 'Centaurus', 'Cepheus', 'Cetus', 'Corona', 'Corvus', 'Crater', 'Cygnus', 'Delphinus', 'Draco', 'Equuleus', 'Eridanus', 'Gemini', 'Hercules', 'Hydra', 'Leo', 'Lepus', 'Libra', 'Lupus', 'Lyra', 'Ophiuchus', 'Orion', 'Pegasus', 'Perseus', 'Pisces', 'Sagittarius', 'Scorpius', 'Serpens', 'Taurus', 'Triangulum', 'Ursa', 'Virgo'), ('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega'))

STAR_LIFETIMES = {'Brown Dwarf': 20.0e9, 'Red Dwarf': 1e12, 'Main Sequence Average Mass': 10e9, 'Main Sequence High Mass': 5e9, 'Giant': 1e9, 'Supergiant': 100e6, 'Hypergiant': 10e6, 'Neutron': 1e12}
STAR_AVERAGE_MASSES = {'Brown Dwarf': 8.75e28, 'Red Dwarf': 5.72e29, 'Main Sequence Average Mass': 1.94e30, 'Main Sequence High Mass': 3.00e30, 'Giant': 1.00e31, 'Supergiant': 7.96e31, 'Hypergiant': 2.50e32, 'Neutron': 2.77e30}
STAR_STDDEV_MASSES = {'Brown Dwarf': 1.5e28, 'Red Dwarf': 1.5e29, 'Main Sequence Average Mass': 1.2e29, 'Main Sequence High Mass': 8e29, 'Giant': 1.2e30, 'Supergiant': 1.5e31, 'Hypergiant': 2.0e31, 'Neutron': 1e29}
STAR_AVERAGE_RADII = {'Brown Dwarf': 90.0e6, 'Red Dwarf': 400.0e6, 'Main Sequence Average Mass': 695.5e6, 'Main Sequence High Mass': 1.0e9, 'Giant': 20.0e9, 'Supergiant': 695.5e9, 'Hypergiant': 1.000e10, 'Neutron': 10e3}
STAR_STDDEV_RADII = {'Brown Dwarf': 10.0e6, 'Red Dwarf': 80.0e6, 'Main Sequence Average Mass': 80.0e6, 'Main Sequence High Mass': 0.3e9, 'Giant': 2.0e9, 'Supergiant': 10.0e9, 'Hypergiant': 0.1e10, 'Neutron': 0.01e3}
STAR_COLORS = {'Brown Dwarf': ['brown'], 'Red Dwarf': ['red'], 'Main Sequence Average Mass': ['yellow'], 'Main Sequence High Mass': ['red', 'blue'], 'Giant': ['red', 'blue'], 'Supergiant': ['red', 'blue'], 'Hypergiant': ['red', 'blue'], 'Neutron': ['white']}
STAR_AVERAGE_TEMPERATURE = {'Brown Dwarf': 800, 'Red Dwarf': 3100, 'Main Sequence Average Mass': 5750, 'Main Sequence High Mass': 8000, 'Giant': 12500, 'Supergiant': 20000, 'Hypergiant': 33000, 'Neutron': 600000}
STAR_STDDEV_TEMPERATURE = {'Brown Dwarf': 200, 'Red Dwarf': 500, 'Main Sequence Average Mass': 800, 'Main Sequence High Mass': 1000, 'Giant': 3000, 'Supergiant': 4000, 'Hypergiant': 8000, 'Neutron': 60000}

PLANET_AVERAGE_NUM_MOONS = {'Gas Giant':20, 'Terrestrial':2, 'Dwarf': 0.78}
PLANET_AVERAGE_MASSES = {'Dwarf': 1.00e21, 'Terrestrial': 5.00e23, 'Gas Giant': 5.00e26}
PLANET_STDDEV_MASSES = {'Dwarf': 0.2e21, 'Terrestrial': 1.0e23, 'Gas Giant': 1.0e26}
PLANET_AVERAGE_RADII = {'Dwarf': 1188e3, 'Terrestrial': 6371e3, 'Gas Giant': 32000e3}
PLANET_STDDEV_RADII = {'Dwarf': 200e3, 'Terrestrial': 1000e3, 'Gas Giant': 8000e3}
PLANET_AVERAGE_ECCENTRICITY = {'Dwarf': 0.1, 'Terrestrial': 0.01, 'Gas Giant': 0.005}
PLANET_STDDEV_ECCENTRICITY = {'Dwarf': 0.08, 'Terrestrial': 0.008, 'Gas Giant': 0.004}
PLANET_AVERAGE_ROTATION_PERIOD = {'Dwarf': 86400, 'Terrestrial': 86400, 'Gas Giant': 40000}
PLANET_STDDEV_ROTATION_PERIOD = {'Dwarf': 43200, 'Terrestrial': 10000, 'Gas Giant': 10000}

PLANET_AVERAGE_INCLINATION = 0.0
PLANET_STDDEV_INCLINATION = 3.0

PLANET_RINGS_TYPES = (('None', 8), ('Single', 4), ('Many', 3))

PLANET_ALL_COLORS = ['gray', 'white', 'yellow', 'tan', 'blue', 'green', 'red', 'maroon', 'pink', 'orange']
PLANET_MIN_COLORS = 1
PLANET_MAX_COLORS = 4

CONST_G = 6.674e-11
