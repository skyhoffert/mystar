// Sky Hoffert
// November 1, 2018

/* CONSTANTS ***********************************************************************************************/
NUM_SAMPLES = 100
SEED_INIT = 1

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

/* MAIN PROGRAM ********************************************************************************************/
