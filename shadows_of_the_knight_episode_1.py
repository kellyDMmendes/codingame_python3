''' You will look for the hostages on a given building by jumping from one
window to another using your grapnel gun. Your goal is to jump to the window
where the hostages are located in order to disarm the bombs. Unfortunately,
you have a limited number of jumps before the bombs go off... '''
from math import ceil

w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
MIN_X = MIN_Y = 0
max_x = w - 1
max_y = h - 1

while True:
    bomb_dir = input()

    if bomb_dir.find("U")>-1:
        max_y = y0 - 1
    elif bomb_dir.find("D")>-1:
        MIN_Y = y0 + 1
    if bomb_dir.find("L")>-1:
        max_x = x0 - 1
    elif bomb_dir.find("R")>-1:
        MIN_X = x0 + 1

    x0 = MIN_X + ceil((max_x  - MIN_X)/2)
    y0 = MIN_Y + ceil((max_y  - MIN_Y)/2)

    print(f"{x0} {y0}")
