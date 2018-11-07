# mystar
Interactive program where users can create their own Star System!

## TODO
Major outstanding tasks that need to be complete are:
 * generate_system.js - Creation of new systems
   * Expand on existing systems and fix any bugs/issues.
   * Match with display format of mystar application
 * mystar application - Create a super simple starting point for displaying and interacting with systems.
   * Complete electron/node js program
   * Think about a way to involve users more - some sort of game? Sharing potential?
 * saving and modifying systems - Allow users to interact and save systems

&nbsp;

---

&nbsp;

## How to Use This Software
Version 0.1 consists of a simple node.js program that generates a random Star System given a seed. This will create a json object and save it to a file with the system name as its title. As long as you download the directory as is, it should have everything it needs to run.

#### Requirements
You need to download some javascript dependencies to run the software, including:
 * node.js
 * npm
 * electron
 * electron-packager

#### Running It
Currently, this library requires npm to run on electron. electron-packager may be used to build a standalone executable, but at the current time the program is not ready for deployment. To test the program, use the command

*npm start*

This will open a window for the application where interaction can occur. To build a standalone executable, use the command

*npm run package-OS*

Where *OS* may be one of "win", "mac", or "linux".

## Seeding Notes
During development, some notable seeds were discovered that had some interesting feature. They are listed below.
* 12 - "3437 Rho-Beta Scorpius" A system with 4 Stars.

## Interacting Notes
There are a few ways to interact with the program at the current time. More will come!
 * Clicking on objects will move the camera to them and display information about a given body on the right pane
 * Dragging the mouse will move the camera anywhere
 * Clicking on the system name in the top right will bring the camera back to the home position
 * Pressing the spacebar will also bring the camera to the home position.

&nbsp;

&nbsp;
