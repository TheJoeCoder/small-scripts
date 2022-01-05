from shapes import *
from random import randint
from PIL import Image

cellwidth = 30
cellheight = 30

image = "cupcake.png"


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

img = Image.open(image)

gridwidth = img.size[0]
gridheight = img.size[1]

paper = Paper(gridwidth * cellwidth, gridheight * cellheight)

for y in range(gridheight):
    for x in range(gridwidth):
        pixel = img.getpixel((x, y))
        if pixel[3] == 0:
            colour = "#FFFFFF"
        else:
            colour = rgb_to_hex((pixel[0], pixel[1], pixel[2]))
        rect = Rectangle(cellwidth, cellheight, x*cellwidth, y*cellheight, colour)
        rect.draw()


paper.display()