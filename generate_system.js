// Sky Hoffert
// November 1, 2018

var constants = require('./constants');

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
    num += diff_mean;
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
    // generate a system name!
    let system_name = generate_system_name();

    let stars = generate_stars(system_name);

    // create the json object
    let system = {'name': system_name, 'stars': stars};

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
    if (star['type'] == 'Main Sequence High Mass' || star['type'] == 'Giant' || star['type'] == 'Supergiant' || star['type'] == 'Hypergiant'){
        temp = temp.splice(Math.round(random(0, 1)), 1);
    }

    return temp;
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
