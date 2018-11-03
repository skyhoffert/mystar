// Sky Hoffert
// November 3, 2018

const generate_system = require('./generate_system');

var c = document.getElementById("main_canvas");
c.width = 1280;
c.height = 720;
var ctx = c.getContext("2d");

var system = null;

// set frame rate to 30 fps
setInterval(update, 1000/30);

// main update function
function update(){
    ctx.fillStyle = 'white';
    ctx.arc(c.width/2, c.height/2, 10, 0, 2*Math.PI);
    ctx.fill();
}

function load_new_system(){
}
