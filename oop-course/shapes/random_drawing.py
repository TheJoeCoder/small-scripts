from shapes import *
from random import randint

paper = Paper()

numshapes = 10

shapes = []

for i in range(numshapes):
    shapes.append(Oval())
    shapes[i].randomize()
    shapes[i].draw()

paper.display()