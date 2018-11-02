# mystar
Interactive program where users can create their own Star System!

## TODO
Major outstanding tasks that need to be complete are:
 * generate_system.js - Complete implementation in javascript
 * mystar application - Create a super simple starting point for displaying and interacting with systems.
   * Decide on visual organization and menu interaction, including uploading old and generating new Systems
   * Figure out how to draw things and choose a style
   * Complete electron/node js program
   * Think about a way to involve users more - some sort of game? Sharing potential?

&nbsp;

---

## python3

### How to Use This Software
Version 0.1 consists of a simple python3 program that generates a random Star System given a seed. This will create a json object and save it to a file with the system name as its title. As long as you download the directory as is, it should have everything it needs to run. 

##### Requirements
You need to download some python3 libraries to run the software, including:
* datetime
* json
* numpy

##### Running It
To run, simple use the command

*python3 generate_system.py <seed>*

Where *<seed>* is replaced with an integer value. Some interesting seeds that my operating system (OS) generated are listed in the "Seeding Notes" section, below.

### Seeding Notes
The *generate_system.py* file can be seeded with a single command line integer argument. Some interesting seeds that I used on my OS are listed below if you would like to experiment with them! I cannot guarantee seeds will generate the same systems (my OS is 64-bit Windows 10).
* 0 - "3732 Pi-Chi Andromeda B" A system with a good mix of planets and stars
* 5 - "3915 Omicron-Pi Serpens A" Neutron star with 13 planets :O

&nbsp;

---

## javascript

### How to Use This Software
Version 0.1 consists of a simple node.js program that generates a random Star System given a seed. This will create a json object and save it to a file with the system name as its title. As long as you download the directory as is, it should have everything it needs to run.

##### Requirements
You need to download some javascript dependencies to run the software, including:
 * node.js

##### Running It
To run, simple use the command

*node generate_system.js <seed>*

Where *<seed>* is replaced with an integer value. Some interesting seeds are listed in the "Seeding Notes" section, below.
**NOTE:** A *<seed>* of 0 will not differ from a seed of 1 for this version

### Seeding Notes
The *generate_system.js* file can be seeded with a single command line integer argument. Some interesting seeds are listed below if you would like to experiment with them! I cannot guarantee seeds will generate the same systems (my OS is 64-bit Windows 10), but given the random number generation, it should work!
* 12 - "3437 Rho-Beta Scorpius" A system with 4 Stars.

&nbsp;

&nbsp;

&nbsp;

