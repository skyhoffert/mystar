# mystar
Interactive program where users can create their own Star System!

## TODO
Major outstanding tasks that need to be complete are:
 * generate_system.js - Expand on existing systems and fix any bugs/issues.
 * mystar application - Create a super simple starting point for displaying and interacting with systems.
   * Decide on visual organization and menu interaction, including uploading old and generating new Systems
   * Figure out how to draw things and choose a style
   * Complete electron/node js program
   * Think about a way to involve users more - some sort of game? Sharing potential?

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

*npm run package-<OS>*

Where *<OS>* may be one of "win", "mac", or "linux".

## Seeding Notes
During development, some notable seeds were discovered that had some interesting feature. They are listed below.
* 12 - "3437 Rho-Beta Scorpius" A system with 4 Stars.

&nbsp;

&nbsp;
