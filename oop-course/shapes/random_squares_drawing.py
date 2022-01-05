from shapes import *
from random import randint

paper = Paper()

cellwidth = 20
cellheight = 20

gridwidth = 30
gridheight = 30


colours = ["red", "green", "blue", "yellow", "orange", "purple"]

for y in range(gridheight):
    for x in range(gridwidth):
        colour = colours[randint(0, len(colours) - 1)]
        rect = Rectangle(cellwidth, cellheight, x*cellwidth, y*cellheight, colour)
        rect.draw()


paper.display()