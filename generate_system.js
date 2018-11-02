// Sky Hoffert
// November 1, 2018

var constants = require('./constants');
var fs = require('fs');

/* CONSTANTS ***********************************************************************************************************/
const NUM_SAMPLES = 100;
const SEED_INIT = 1;

/* GLOBAL VARIABLES ****************************************************************************************************/
var seed = SEED_INIT;

/* FUNCTIONS ***********************************************************************************************************/
// Standard Normal variate using Box-Muller transform.
function random_bm(mean=0.5, sigma=0.125) {
    let u = 0, v = 0;
    while(u === 0) u = random(); //Converting [0,1) to (0,1)
    while(v === 0) v = random();
    let num = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v );
    num = num / 10.0 + 0.5; // Translate to 0 -> 1
    let diff_mean = mean - 0.5;
    let diff_stddev = sigma / 0.125;
    // bring value down to be around 0 and scale/translate
    num -= 0.5;
    num *= diff_stddev;
    num += diff_mean + 0.5;
    return num;
}

// Random uniform value between 0 and 1
function random(min=0, max=1) {
    let x = Math.sin(seed++) * 10000;
    x = x - Math.floor(x);
    let range = max - min;
    x *= range;
    x += min;
    return x;
}

/*
Returns the dict describing the parent star of a given planet in a given system
    @arg planet: dict; describes the target planet
    @arg system: dict; describes the target star
    @return: dict; describing the parent star
*/
function find_parent_star(planet, system){
    // search the system for the parent
    for (let i = 0; i < system['stars'].length; i++){
        if (planet['parent'] == system['stars'][i]['name']){
            return system['stars'][i];
        }
    }
    
    // if no parent is found, return None
    return null;
}

/*
Calculates orbital clearing given certain planet parameters
    @arg planet: dict; describes the target planet
    @arg system: dict; describes the target system
    @return: float; orbital clearing distance in m
*/
function calculate_orbital_clearing(planet, system){
    let a = planet['semi_major_axis'];
    let m = planet['mass'];
    let M = find_parent_star(planet, system)['mass'];

    let r_soi = a * (m / M)**(2/5);
    let clearing = r_soi * constants.ORBIT_CLEAR_FACTOR;

    if (clearing < constants.ORBIT_CLEAR_INCREASE_LIMIT){
        clearing *= constants.ORBIT_CLEAR_INCREASE_FACTOR;
    }

    return clearing;
}

// round a floating point value with given significant figures
function round_to_sigfigs(val, sigfigs){
    return Number.parseFloat(val.toPrecision(sigfigs));
}

// actual specific generation functions ****
/*
Main function for system generation. This will use all other functions to create a system.
    @return dict; describing the generated system
*/
function generate_system(){
    // create the dict
    let system = {};

    // generate a system name and Stars!
    system['name'] = generate_system_name();
    system['stars'] = generate_stars(system['name']);
    
    // at this point we generate an age in years
    let longest = 13.7e9;
    let i = 0;

    // check every Star given for longest possible age
    for (i = 0; i < system['stars'].length; i++){
        longest = constants.STAR_LIFETIMES[system['stars'][i]['type']] < longest ? constants.STAR_LIFETIMES[system['stars'][i]['type']] : longest;
    }

    system['age'] = Math.round(random(0, 1) * longest);

    // include some basic values in the system
    system['discovered_by'] = 'sky';
    system['date_discovered'] = new Date().toISOString().replace('-', '/').split('T')[0].replace('-', '/');
    system['planets'] = [];

    // generate the planets of this system
    let num_planets = generate_value_from_list(constants.NUM_PLANETS);
    for (i = 0; i < num_planets; i++){
        let type = generate_value_from_list(constants.PLANET_TYPES)
        system['planets'].push(generate_planet_details(type, system));
    }

    return system;
}

/* 
Returns a value from a predefined list meeting the proper format
    @arg list: list; holds values that match the format (value, weight)
    @return: variable; the "random" value generated
*/
function generate_value_from_list(list){
    // first, calculate the total value of all weights
    var total_dist = 0;
    var i = 0;
    for (i = 0; i < list.length; i++){
        total_dist += list[i][1];
    }
    
    // generate a random value
    var val = random(0,1) * total_dist;
    var total_running = 0;
    
    // now, find which type based on that random value
    for (i = 0; i < list.length; i++){
        total_running += list[i][1];
        if (val < total_running){
            return list[i][0];
        }
    }
    return list[0][0]
}

/* 
Generates a new, random system name!
    @return: string; name of a new system
*/
function generate_system_name(){
    let system_name  = String(Math.floor(1000 + random(0, 9000)));
    system_name += ' ' + String(constants.SYSTEM_NAMES[1][Math.floor(random(0, constants.SYSTEM_NAMES[1].length))]);
    system_name += '-' + String(constants.SYSTEM_NAMES[1][Math.floor(random(0, constants.SYSTEM_NAMES[1].length))]);
    system_name += ' ' + String(constants.SYSTEM_NAMES[0][Math.floor(random(0, constants.SYSTEM_NAMES[0].length))]);

    return system_name;
}

/*
Generates Stars for a given system and names them appropriately.
    @arg name: string; name of the system
    @return: array; of Stars
*/
function generate_stars(system_name){
    // generate number of Stars
    let num_stars = generate_value_from_list(constants.NUM_STARS);

    let stars = [];
    let star_types = [];
    let star_letter_int = 'A'.charCodeAt(0);
    let i = 0;
    for (i = 0; i < num_stars; i++){
        let star_type = generate_value_from_list(constants.STAR_TYPES);
        let details = generate_star_details(star_type);
        let name = system_name + ' ' + String.fromCharCode(star_letter_int);
        details['name'] = name;
        star_letter_int += 1;
        stars.push(details);
    }

    return stars;
}

/*
Generates a dictionary object that fully describes a new Star
    @arg s: string; describes the type of Star
    @return: dict; all details about the new Star
*/
function generate_star_details(s){
    let star = {};

    star['type'] = s;
    star['mass'] = round_to_sigfigs(random_bm(constants.STAR_AVERAGE_MASSES[s], constants.STAR_STDDEV_MASSES[s]), 4);
    star['radius'] = generate_star_radius(s, star['mass']);
    star['surface_temperature'] = generate_star_temperature(s, star['mass'], star['radius']);
    star['parent'] = '';
    star['colors'] = generate_star_colors(star);
    star['alternate_names'] = [];

    return star;
}

/* STAR GENERATION *****************************************************************************************************/
/*
Generates the radius of a given type of Star, depending on the Mass
    @arg s: string; the type of Star provided
    @arg mass: int; mass of the given Star in kg to correlate a radius to
    @return: int; radius of given Star in meters
*/
function generate_star_radius(s, mass){
    // use the difference in mass to calculate a correlated difference in radius
    let num_stddevs_away = (mass - constants.STAR_AVERAGE_MASSES[s]) / constants.STAR_STDDEV_MASSES[s];
    let radius = constants.STAR_AVERAGE_RADII[s]  + constants.STAR_STDDEV_RADII[s] * num_stddevs_away * random_bm(1,0.1);

    return round_to_sigfigs(radius, 4);
}

/*
Generate the temperature of a given type of Star, depending on Mass and Radius
    @arg s: string; the type of Star provided
    @arg mass: int; mass of the given Star in kg
    @arg radius: int; radius of the given Star in m
    @return: int; temperature of given star in Kelvin
*/
function generate_star_temperature(s, mass, radius){
    let num_stddevs_away = (mass - constants.STAR_AVERAGE_MASSES[s]) / constants.STAR_STDDEV_MASSES[s];
    let temp = constants.STAR_AVERAGE_TEMPERATURE[s] + constants.STAR_STDDEV_TEMPERATURE[s] * num_stddevs_away * random_bm(1,0.1);

    return Math.round(temp);
}

/*
Generates colors of a Star, given the type
    @arg star: dict; describes the Star
    @return: list; of colors describing the Star
*/
function generate_star_colors(star){
    // fetch the predefined possible colors
    let temp = constants.STAR_COLORS[star['type']];
    
    // remove wrong colors if giant type
    if (star['type'] === 'Main Sequence High Mass' || star['type'] === 'Giant' || star['type'] === 'Supergiant' || star['type'] === 'Hypergiant'){
        temp = temp.splice(Math.round(random(0, 1)), 1);
    }

    return temp;
}

/* PLANET GENERATION ***************************************************************************************************/
/*
Generates a dictionary object that fully describes a new planet
    @arg p: string; describes the type of planet
    @arg system: dict; describes the entire system
    @return: dict; all details about the new planet
*/
function generate_planet_details(p, system){
    let planet = {};

    // name is set first to a ? to indicate it is being modified
    planet['name'] = '?';

    planet['type'] = p;
    planet['parent'] = system['stars'][Math.round(random(0,system['stars'].length-1))]['name'];
    
    // now that the planet has a parent, it can be named properly
    planet['name'] = generate_planet_name(system, planet['parent']);
    
    planet['mass'] = round_to_sigfigs(random_bm(constants.PLANET_AVERAGE_MASSES[p], constants.PLANET_STDDEV_MASSES[p]), 4);
    planet['radius'] = generate_planet_radius(p, planet['mass']);
    planet['semi_major_axis'] = generate_planet_sma(planet, system);
    planet['eccentricity'] = Math.abs(round_to_sigfigs(random_bm(constants.PLANET_AVERAGE_ECCENTRICITY[p], constants.PLANET_STDDEV_ECCENTRICITY[p]), 4));

    // the first planet in any system will have 0 inclination, the rest will have relative
    if (planet['name'].substr(-1) == 'a'){
        planet['inclination'] = 0.0;
    } else {
        planet['inclination'] = round_to_sigfigs(random_bm(constants.PLANET_AVERAGE_INCLINATION, constants.PLANET_STDDEV_INCLINATION), 4);
    }
    
    planet['rotation_period'] = generate_planet_rotation_period(planet);
    planet['axial_tilt'] = round_to_sigfigs(random_bm(constants.PLANET_AVERAGE_AXIAL_TILT[p], constants.PLANET_STDDEV_AXIAL_TILT[p]), 4);
    planet['albedo'] = Math.abs(round_to_sigfigs(random_bm(constants.PLANET_AVERAGE_ALBEDO[p], constants.PLANET_STDDEV_ALBEDO[p]), 4));
    planet['surface_pressure'] = generate_planet_surface_pressure(planet);
    planet['surface_temperature'] = generate_planet_temp(planet, system);
    planet['colors'] = generate_planet_colors(planet);

    planet['rings'] = [];
    planet['moons'] = [];
    planet['alternate_names'] = [];
    
    // Moons:
    let avg = constants.PLANET_AVERAGE_NUM_MOONS[p];
    // use a normal curve with mean equal to average and a fitting stddev
    let num_moons = Math.abs(Math.floor(random_bm(avg,avg/2)));
    // special case, if gas giant, add minimum number of moons!
    if (planet['type'] === 'Gas Giant'){
        num_moons += constants.PLANET_AVERAGE_NUM_MOONS[planet['type']];
    }
    // TODO - Add moons!

    // Rings:
    // only applies to gas giants!
    if (planet['type'] == 'Gas Giant'){
        // TODO: add chance for rings to gas giants
    }

    return planet
}

/*
Generates a planet name given the system and parent
    @arg system: dict; describes the entire system
    @arg parent: dict; describes the parent object
    @return: string; name for the planet
*/
function generate_planet_name(system, parent){
    // keep track of how many children the parent has
    let num_parent_children = 0;
    let i = 0;

    // loop through all planets in the system
    for (i = 0; i < system['planets'].length; i++){
        // detect if this planet is the one we are naming
        if (system['planets'][i]['name'] === '?'){
            continue;
        }

        // otherwise, check if the parent has other children
        if (system['planets'][i]['parent'] === parent){
            num_parent_children += 1;
        }
    }

    // add a lowercase letter to indicate a planet
    return parent + String.fromCharCode('a'.charCodeAt(0) + num_parent_children);
}

/*
Generates a planet radius, given the type of planet and mass
    @arg p: string; indicates the type of planet
    @arg mass: int; mass of the given planet in kg
    @return: int; value for radius of given planet
*/
function generate_planet_radius(p, mass){
    // use the difference in mass to calculate a correlated difference in radius
    let num_stddevs_away = (mass - constants.PLANET_AVERAGE_MASSES[p]) / constants.PLANET_STDDEV_MASSES[p];
    let radius = constants.PLANET_AVERAGE_RADII[p] + constants.PLANET_STDDEV_RADII[p] * num_stddevs_away * random_bm(1,0.1);

    return Math.round(radius)
}

/*
Generates a planet orbital radius (semi-major-axis), given the planet and system
    @arg planet: dict; describes the given planet
    @arg system: dict; describes the entire system
    @return: int; orbital radius value in meters
*/
function generate_planet_sma(planet, system){
    // Loop until a good sma is found
    let passing = false;
    let sma = 0;
    while (!passing){
        sma = Math.abs(random_bm(0.5,1)*constants.SEMI_MAJOR_AXIS_FACTOR + constants.SEMI_MAJOR_AXIS_OFFSET);
        passing = true;
        for (let i = 0; i < system['planets'].length; i++){
            if (planet['parent'] === system['planets'][i]['parent']){
                let this_clearance = calculate_orbital_clearing(planet, system);
                let p_clearance = calculate_orbital_clearing(system['planets'][i], system);
                let max_sma = system['planets'][i]['semi_major_axis'] - p_clearance - this_clearance;
                let min_sma = system['planets'][i]['semi_major_axis'] + p_clearance + this_clearance;
                if (sma > max_sma && sma < min_sma){
                    passing = false;
                    break;
                }
            }
        }
    }

    return Math.round(sma);
}

/*
Generates a rotational period
    @arg planet: dict; describes the target planet
    @return: float; rotational period in seconds
*/
function generate_planet_rotation_period(planet){
    // first, find the average and stddev for each type
    let mean = constants.PLANET_AVERAGE_ROTATION_PERIOD[planet['type']];
    let stddev = constants.PLANET_STDDEV_ROTATION_PERIOD[planet['type']];
    let rot_per = Math.abs(random_bm(mean, stddev));

    // make some planets randomly have retrograde rotation, not gas giants though
    if (planet['type'] === 'Dwarf' || planet['type'] === 'Gas Giant'){
        if (random(0.0, 1.0) < constants.PLANET_RETROGRADE_CHANCE){
            // retrograde rotations probably have longer rotation rates as well
            rot_per *= -constants.PLANET_RETROGRADE_LENGTH_INCREASE;
        }
    }

    return Math.round(rot_per)
}

/*
Generates a surface pressure for the given planet
    @arg planet: dict; describes the target planet
    @return: float; surface pressure in kPa
*/
function generate_planet_surface_pressure(planet){
    let mean = constants.PLANET_AVERAGE_PRESSURE[planet['type']];
    let stddev = constants.PLANET_STDDEV_PRESSURE[planet['type']];

    let P = random_bm(mean, stddev);
    // if negative, approach 0 as the inverse
    if (P < 0){
        P = 1 / -P;
    }
    
    return round_to_sigfigs(P, 6);
}

/*
Generates a minimum surface temperature for the given planet
    @arg planet: dict; describes the target planet
    @return: float; minimum surface temperature in Kelvin
*/
// TODO - fix this function, temperatures are not correct
function generate_planet_temp(planet, system){
    // Use the properties of the parent star
    let R_star = find_parent_star(planet, system)['radius'];
    let T_star = find_parent_star(planet, system)['surface_temperature'];
    // Luminosity formula
    let L_star = 4 * 3.14159 * R_star**2 * constants.STEFAN_BOLTZMANN_CONSTANT * T_star**4;
    // Radiative Equilibrium Temperature formula
    let T = (L_star * (1 - planet['albedo']) / (16 * 3.14159 * planet['semi_major_axis']**2 * constants.STEFAN_BOLTZMANN_CONSTANT))**(1/4);

    return round_to_sigfigs(T, 3);
}

/*
Generates a list of colors to associate with the given planet
    @arg planet: dict; describes the planet
    @return: list; colors that should be attached to the planet
*/
function generate_planet_colors(planet){
    let colors = [];

    // randomly (uniformly) select a number of colors
    let num = random(constants.PLANET_MIN_COLORS, constants.PLANET_MAX_COLORS);

    // iterate through as many as was chosen
    for (let i=0; i < num; i++){
        let color = constants.PLANET_ALL_COLORS[Math.round(random(0, constants.PLANET_ALL_COLORS.length))];
        console.log(color);
        if (!colors.includes(color)){
            colors.push(color);
        }
    }

    return colors;
}

/* MAIN PROGRAM ********************************************************************************************************/
 // Modify the seed, if given as a command line argument
 if (process.argv[2] != null){
    const intval = parseInt(process.argv[2], 10);
    if (intval){
        seed = intval;
    }
}

// call the generation function
system = generate_system();

// print it out
system_json = JSON.stringify(system, null, 2);
console.log(system_json);
fs.writeFile('systems/' + system['name'] + '.json', system_json, 'utf8', function(err){
        if (err) throw err;
});

module.exports = {
    new_system: function(sd=(new Date().getTime())){
        seed = sd;
        return generate_system();
    }
}