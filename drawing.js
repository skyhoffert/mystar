// Sky Hoffert
// November 3, 2018

// require the generation script
const generate_system = require('./generate_system');

// grab the canvas from the html document and set things for it
var c = document.getElementById("main_canvas");
c.width = 1280;
c.height = 720;
var ctx = c.getContext("2d");

// keep track of the current system
var system = null;

// set frame rate to 30 fps
setInterval(update, 1000/30);

// main update function
function update(){
    // clear the screen
    ctx.clearRect(0, 0, c.width, c.height);

    // draw stars near the center
    draw_stars();

    // draw planets elsewhere
    draw_planets();
}

/*
Draw stars for the global system variable
    @return: void
*/
function draw_stars(){
    if (system){
        if (system['stars'].length === 1){
            ctx.beginPath();
            ctx.fillStyle = system['stars'][0]['colors'][0];
            ctx.arc(c.width/2, c.height/2, radius_of(system['stars'][0]), 0, 2*Math.PI);
            ctx.fill();
        } else if (system['stars'].length === 2){
            draw_star(system['stars'][0]['colors'][0], c.width/2-15, c.height/2-15, radius_of(system['stars'][0]));
            draw_star(system['stars'][1]['colors'][0], c.width/2+15, c.height/2+15, radius_of(system['stars'][1]));
        } else if (system['stars'].length === 3){
            draw_star(system['stars'][0]['colors'][0], c.width/2-45, c.height/2+15, radius_of(system['stars'][0]));
            draw_star(system['stars'][1]['colors'][0], c.width/2-15, c.height/2+45, radius_of(system['stars'][1]));
            draw_star(system['stars'][2]['colors'][0], c.width/2+30, c.height/2-30, radius_of(system['stars'][2]));
        } else if (system['stars'].length === 4){
            draw_star(system['stars'][0]['colors'][0], c.width/2-45, c.height/2+15, radius_of(system['stars'][0]));
            draw_star(system['stars'][1]['colors'][0], c.width/2-15, c.height/2+45, radius_of(system['stars'][1]));
            draw_star(system['stars'][2]['colors'][0], c.width/2+15, c.height/2-45, radius_of(system['stars'][2]));
            draw_star(system['stars'][3]['colors'][0], c.width/2+45, c.height/2-15, radius_of(system['stars'][3]));
        }
    }
}

/*
Draw stars for the global system variable
    @arg color: string; 6-digit hex value (Ex. #AB1234) or color mapping (Ex. red) representing star color
    @arg x: int; center of star, x
    @arg y: int; center of star, y
    @arg r: int; radius of star, in pixels
    @return: void
*/
function draw_star(color, x, y, r){
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.arc(x, y, r, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();
}

/*
Draw planets for the global system variable
    @return: void
*/
function draw_planets(){
    for (let i = 0; i < system['planets'].length; i++){
        ctx.beginPath();
        ctx.fillStyle = system['planets'][i]['colors'][0];
        ctx.arc(planet_x_by_i(i), c.height/2, 2, 0, 2*Math.PI);
        ctx.fill();
        ctx.closePath();
    }
}

/*
Return a position for planet at given index. This function is temporary TODO
    @return: int; position of planet on screen in pixels
*/
function planet_x_by_i(i){
    // even numbers are on the right side
    return i % 2 === 0 ? c.width/2 + ((i/2)*25 + 200) : c.width/2 - ((i/2)*25 + 200);
}

/*
Calculate and return radius for a given type of star
    @arg star: dict; describing the target star
    @return: int; radius of star in pixels
*/
function radius_of(star){
    if (star['type'] == 'Brown Dwarf'){
        return 8;
    } else if (star['type'] === 'Red Dwarf'){
        return 10;
    } else if (star['type'] === 'Main Sequence Average Mass'){
        return 12;
    } else if (star['type'] === 'Main Sequence High Mass'){
        return 14;
    } else if (star['type'] === 'Giant'){
        return 16;
    } else if (star['type'] === 'Supergiant'){
        return 18;
    } else if (star['type'] === 'Hypergiant'){
        return 20;
    } else /* Neutron Star */ {
        return 6;
    }
}

/*
Loads a new star system using the generate_system file into the global system variable
    @return: void;
*/
function load_new_system(){
    system = generate_system.new_system();

    document.getElementById('system_name').innerHTML = system['name'];
}
