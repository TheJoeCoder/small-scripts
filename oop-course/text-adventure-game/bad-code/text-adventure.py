from adventurecreator import *

game = Game()
game.addroom((0, 0), Room("Kitchen", "This room has nothing in it."))
game.addroom((0, 1), Room("Living Room", "There is nothing here."))

while True:
    print(game.getroom().getname())
    print(game.getroom().getdescription())
    print("Directions you can move:")
    if game.canmove(Direction.NORTH):
        print("- North")
    if game.canmove(Direction.EAST):
        print("- East")
    if game.canmove(Direction.SOUTH):
        print("- South")
    if game.canmove(Direction.WEST):
        print("- West")
    inp = input("Where to move? ")
    try:
        if Direction(inp.upper()) is not None:
            game.move(Direction(inp.upper()))
        else:
            print("You cannot move this way")
    except ValueError:
        print("You cannot move this way")