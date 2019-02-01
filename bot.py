import Coordinates
from numpy import *
import pyautogui
import time
import sys
from PIL import ImageOps, ImageGrab
import os

# Global variables
start = time.time()
counter = 0
ops = 0
modify_by = 0
cactus_coords = Coordinates.cactus()

# Constants
EMPTY_CACTUS_SUM = 3307
PYCHARM_BG_COLOUR = 3103
FILLED_REPLAY_BTN_SUM = 1287


def update_cactus_coords(x):
    global cactus_coords
    cactus_coords = Coordinates.cactus()[0] + x, Coordinates.cactus()[1], \
                    Coordinates.cactus()[2] + x, Coordinates.cactus()[3]
    print('Coordinates are: ', cactus_coords)


def time_modifier():
    global modify_by, cactus_coords
    time_since_start = int(time.time() - start)
    if time_since_start % 10 == 0:
        if time_since_start == 10:
            modify_by = 3
            update_cactus_coords(modify_by)
        elif time_since_start == 20:
            modify_by = 6
            update_cactus_coords(modify_by)
        elif time_since_start == 30:
            modify_by = 9
            update_cactus_coords(modify_by)
        elif time_since_start == 40:
            modify_by = 12
            update_cactus_coords(modify_by)
        elif time_since_start == 50:
            modify_by = 15
            update_cactus_coords(modify_by)
        elif time_since_start == 60:
            modify_by = 18
            update_cactus_coords(modify_by)
        elif time_since_start == 70:
            modify_by = 21
            update_cactus_coords(modify_by)
        elif time_since_start == 80:
            modify_by = 24
            update_cactus_coords(modify_by)
        elif time_since_start == 90:
            modify_by = 27
            update_cactus_coords(modify_by)
        elif time_since_start == 100:
            modify_by = 30
            update_cactus_coords(modify_by)
        elif time_since_start == 110:
            modify_by = 33
            update_cactus_coords(modify_by)
        elif time_since_start == 120:
            modify_by = 36
            update_cactus_coords(modify_by)
        elif time_since_start == 130:
            modify_by = 39
            update_cactus_coords(modify_by)
        elif time_since_start == 140:
            modify_by = 42
            update_cactus_coords(modify_by)
        elif time_since_start == 150:
            modify_by = 45
            update_cactus_coords(modify_by)
        elif time_since_start == 160:
            modify_by = 48
            update_cactus_coords(modify_by)
        elif time_since_start == 170:
            modify_by = 51
            update_cactus_coords(modify_by)
        elif time_since_start == 180:
            modify_by = 54
            update_cactus_coords(modify_by)
        elif time_since_start == 190:
            modify_by = 57
            update_cactus_coords(modify_by)
        elif time_since_start == 200:
            modify_by = 60
            update_cactus_coords(modify_by)

    print('Modified by: ', modify_by)


def loop_counter():
    global counter, ops
    counter += 1
    ops += 1


def cleanup_files():
    dir = os.path.dirname(os.path.realpath(__file__))
    files = os.listdir(dir)
    for file in files:
        if file.endswith(".jpg"):
            os.remove(os.path.join(dir, file))


def image_sum(coords):
    img = ImageGrab.grab(coords)
    grey = ImageOps.grayscale(img)
    sum = array(grey.getcolors()).sum()
    """if coords == Coordinates.cactus():
        filename = str(counter) + '.jpg'
        if sum != EMPTY_CACTUS_SUM:
            filename = 'TREE_' + str(counter) + '.jpg'
        img.save(filename, "JPEG")"""
    return sum


def check_for_cactus():
    global cactus_coords
    sum = image_sum(cactus_coords)
    print('Cactus sum: ', sum)
    if sum == PYCHARM_BG_COLOUR:
        sys.exit(0)

    if sum != EMPTY_CACTUS_SUM:
        print('!!!!!!!!!!!!! Cactus found!')
        return True


def is_game_over():
    if int(time.time() - start) % 8 == 0:
        # pyautogui.click(Coordinates.replaybuttonclick())
        sys.exit(0)
        return True


def action():
    if int(time.time() - start) < 70:
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')
    else:
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')
        time.sleep(0.05)
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')


def main():
    # Cleanup old screen shot files
    cleanup_files()
    while True:
        loop_counter()
        time_modifier()
        if check_for_cactus():
            action()
        #is_game_over()


if __name__ == '__main__':
    main()
