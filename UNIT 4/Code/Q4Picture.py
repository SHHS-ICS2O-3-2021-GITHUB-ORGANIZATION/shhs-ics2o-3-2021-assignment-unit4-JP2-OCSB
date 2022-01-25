# NAME OF AUTHOR:  Jake Pommainville
# NAME OF THE PROGRAM:  Picture
# DATE OF CREATION:  24/1/2022
# PURPOSE OF PROGRAM:  Draws shapes in a pygame window
import pygame, sys
from pygame import Color, draw, display, time

# starts py game
pygame.init()
clock = time.Clock()
# sets game resolution (can change to anything you want so long as its 30+, 30+)
res = (600, 400)
gameDisplay = display.set_mode(res)

# def both shapes pos
x = 30
y = 30
x1 = res[0]-30
y1 = 0

# def radius for the circle
radius = 30

# def direction variables for both shapes
directionx = 0
directiony = 0
directionx1 = 1
directiony1 = 0

# def the colors of the images drawn on the screen
backgroundcolor = 'black'
circlecolor = 'purple'
rectanglecolor = 'red'

while True:
    # makes Closing work smoothly, and x button function
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    # sets background color
    gameDisplay.fill(Color(backgroundcolor))

    # draws the 2 different shapes
    draw.circle(gameDisplay, Color(circlecolor), (x, y), radius)
    draw.rect(gameDisplay, Color(rectanglecolor), (x1, y1, 30, 30))

    # makes it show up
    display.flip()

    # moves the shapes, and chooses their direction
    if x1 == res[0]-30:
        directionx1 = 1
    elif x1 == 0:
        directionx1 = 0
    if y1 == res[1]-30:
        directiony1 = 1
    elif y1 == 0:
        directiony1 = 0
    if x == res[0]-30:
        directionx = 1
    elif x == 30:
        directionx = 0
    if y == res[1]-30:
        directiony = 1
    elif y == 30:
        directiony = 0
    if directionx1 == 0:
        x1 = x1 + 1
    else:
        x1 = x1 - 1
    if directiony1 == 0:
        y1 = y1 + 1
    else:
        y1 = y1 - 1
    if directionx == 0:
        x = x + 1
    else:
        x = x - 1
    if directiony == 0:
        y = y + 1
    else:
        y = y - 1

    clock.tick(60)
