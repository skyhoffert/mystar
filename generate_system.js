// Sky Hoffert
// November 1, 2018

var constants = require('./constants');

/* CONSTANTS ***********************************************************************************************/
const NUM_SAMPLES = 100
const SEED_INIT = 1

/* GLOBAL VARIABLES ****************************************************************************************/
var seed = SEED_INIT;

/* FUNCTIONS ***********************************************************************************************/
// Standard Normal variate using Box-Muller transform.
function random_bm(mean=0.5, sigma=0.125) {
    let u = 0, v = 0;
    while(u === 0) u = random(); //Converting [0,1) to (0,1)
    while(v === 0) v = random();
    let num = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v );
    num = num / 10.0 + 0.5; // Translate to 0 -> 1
    let diff_mean = mean - 0.5;
    let diff_stddev = sigma / 0.125
    num += diff_mean
    num *= diff_stddev
    return num
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

// actual specific generation functions ****

/*
Main function for system generation. This will use all other functions to create a system.
    @return dict; describing the generated system
*/
function generate_system(){
    // generate a system name!
    let system_name = generate_system_name();

    // generate number of Stars
    let num_stars = generate_value_from_list(constants.NUM_STARS);

    let system = {'name': system_name, 'num_stars': num_stars};

    return system;
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

// DEBUG
function DEBUG(msg){
    console.log('DEBUG: ' + msg)
}

/* MAIN PROGRAM ********************************************************************************************/
 // Modify the seed, if given as a command line argument
 if (process.argv[2] != null){
    const intval = parseInt(process.argv[2], 10)
    if (intval){
        seed = intval
    }
}

system = generate_system();
system_json = JSON.stringify(system);

console.log(system_json)
