// Sky Hoffert
// November 1, 2018

var constants = require('./constants');

/* CONSTANTS ***********************************************************************************************/
const NUM_SAMPLES = 100
const SEED_INIT = 1

/* GLOBAL VARIABLES ****************************************************************************************/
var seed = SEED_INIT;

/* FUNCTIONS ***********************************************************************************************/
function generate_system_name(){
    let system_name  = String(Math.floor(1000 + random(0, 9000)));
    system_name += ' ' + String(constants.SYSTEM_NAMES[1][Math.floor(random(0, constants.SYSTEM_NAMES[1].length))]);
    system_name += '-' + String(constants.SYSTEM_NAMES[1][Math.floor(random(0, constants.SYSTEM_NAMES[1].length))]);
    system_name += ' ' + String(constants.SYSTEM_NAMES[0][Math.floor(random(0, constants.SYSTEM_NAMES[0].length))]);

    return system_name;
}
// Standard Normal variate using Box-Muller transform.
function random_bm(mean=0.5, sigma=0.125) {
    let u = 0, v = 0;
    while(u === 0) u = random(); //Converting [0,1) to (0,1)
    while(v === 0) v = random();
    let num = Math.sqrt( -2.0 * Math.log( u ) ) * Math.cos( 2.0 * Math.PI * v );
    num = num / 10.0 + 0.5; // Translate to 0 -> 1
    let diff_mean = mean - 0.5;
    let diff_stddev = sigma / 0.125
    num = num + diff_mean
    num = num * diff_stddev
    return num
}

// Random uniform value between 0 and 1
function random(min=0, max=1) {
    let x = Math.sin(seed++) * 10000;
    x = x - Math.floor(x);
    let range = max - min;
    x = x * range;
    x = x + min;
    return x;
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

// generate a system name!
name = generate_system_name();

console.log(name)
