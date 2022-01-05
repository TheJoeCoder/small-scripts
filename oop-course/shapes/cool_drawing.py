from shapes import *

# Define colours
cakesponge, cherry, cakeholder = "#C77F30", "#ED1D24", "#E688B1"

# Define the paper
paper = Paper()

# Make a list to store shapes
shapes = []

# Define shapes (lowest layer first)
shapes.append(Rectangle(600, 600, 0, 0, "black")) # Background
shapes.append(Oval(400, 400, 100, 100, cakesponge)) # Main cake bit
shapes.append(Oval(80, 80, 260, 40, cherry)) # Cherry

# Draw them all then render it
for shape in shapes:
    shape.draw()

paper.display()