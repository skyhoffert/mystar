# mystar
Interactive program where users can create their own Star System!

## How to Use This Software
Version 0.1 consists of a simple python3 program that generates a random Star System given a seed. This will create a json object and save it to a file with the system name as its title. As long as you download the directory as is, it should have everything it needs to run. 

#### Requirements
You need to download some python3 libraries to run the software, including:
* datetime
* json
* numpy

#### Running It
To run, simple use the command

*python3 generate_system.py <seed>*

Where *<seed>* is replaced with an integer value. Some interesting seeds that my operating system (OS) generated are listed in the "Seeding Notes" section, below.

## Seeding Notes
The *generate_system.py* file can be seeded with a single command line integer argument. Some interesting seeds that I used on my OS are listed below if you would like to experiment with them! I cannot guarantee seeds will generate the same systems (my OS is 64-bit Windows 10).
* 0 - "3732 Pi-Chi Andromeda B" A system with a good mix of planets and stars
* 5 - "3915 Omicron-Pi Serpens A" Neutron star with 13 planets :O