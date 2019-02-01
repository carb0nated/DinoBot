# DinoBot
A bot which playes the T-Rex dino game from Google Chrome's offline mode.


## How does it work?
DinoBot captures screenshots at certain (variable) positions and converts the data into an array of grayscale pixels. It then
calculates the sum of these pixels to determine whether an object, such as a cactus or a bat, is going to block our path. Then, 
depending on how long you've been running the game for, it modifies where to look on the screen, when to jump and whether it needs 
to land as soon as possible or to just take its time.


## Requirements
The bot was tested and confirmed to work properly under the following conditions.
* At least Python 3.6 installed
* Monitor resolution set at 1920x1080 pixels

This bot was only tested using Google Chrome, but should work using most browsers.


## Installation & Usage
***Make sure you check the requirements above before proceeding with the installation.***

1- Clone/download the repository to a directory of your choice

2- Visit http://www.trex-game.skipser.com/ 

3- Launch `bot.py` in the same directory as `Coordinates.py`

4- Switch back to the game window as soon as possible and hit space to start the game

5- Sit back, relax, and let your computer play the game for you!
