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
STAR_AVERAGE_MASSES = {'Brown Dwarf': 8.75e28, 'Red Dwarf': 5.72e29, 'Main Sequence Average Mass': 1.00e30, 'Main Sequence High Mass': 3.00e30, 'Giant': 1.00e31, 'Supergiant': 7.96e31, 'Hypergiant': 2.50e32, 'Neutron': 2.77e30}
STAR_STDDEV_MASSES = {'Brown Dwarf': 1.5e28, 'Red Dwarf': 1.5e29, 'Main Sequence Average Mass': 1.2e29, 'Main Sequence High Mass': 0.8e30, 'Giant': 1.2e30, 'Supergiant': 1.5e31, 'Hypergiant': 2.0e31, 'Neutron': 1e29}

PLANET_AVERAGE_NUM_MOONS = {'Gas Giant':20, 'Terrestrial':2, 'Dwarf': 0.78}
PLANET_AVERAGE_MASSES = {'Dwarf': 1.00e21, 'Terrestrial': 5.00e23, 'Gas Giant': 5.00e26}
PLANET_STDDEV_MASSES = {'Dwarf': 0.8, 'Terrestrial': 0.6, 'Gas Giant': 0.8}