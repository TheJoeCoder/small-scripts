from turtle import *
from math import *

sides = int(input("How many sides?\n> "))
color(input("What colour?\n> "))

for i in range(sides):
  forward(floor(360/sides/1.02))
  left(360/sides)
