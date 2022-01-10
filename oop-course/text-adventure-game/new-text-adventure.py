from enum import Enum, auto

class Direction(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

    def opposite(self):
        if self is Direction.NORTH:
            return Direction.SOUTH
        if self is Direction.SOUTH:
            return Direction.NORTH
        if self is Direction.EAST:
            return Direction.WEST
        if self is Direction.WEST:
            return Direction.EAST

class Room():
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = "No description"
        self.linkedrooms = {}
    def get_name(self) -> str:
        return self.name
    def get_description(self) -> str:
        return self.description
    def set_description(self, description: str) -> None:
        self.description = description
    def get_linked_room(self, direction: Direction):
        try:
            return self.linkedrooms[direction]
        except KeyError:
            return None
    def link_room(self, direction: Direction, room_to_link) -> None:
        self.linkedrooms[direction] = room_to_link
    def print_details(self):
        print(self.name + "\n---\n" + self.description + "\n---")
        for direction in self.linkedrooms:
            room = self.linkedrooms[direction]
            print("The " + room.get_name() + " is " + direction.name.lower())
        print("----------")

def link_bidirectional(first: Room, second: Room, direction: Direction):
    first.link_room(direction, second)
    second.link_room(direction.opposite(), first)

kitchen = Room("Kitchen")
kitchen.set_description("A solitary place.")

diningroom = Room("Dining Room")
diningroom.set_description("There is a potato on a chair.")

ballroom = Room("Ballroom")
ballroom.set_description("There are people dancing.")

link_bidirectional(kitchen, diningroom, Direction.SOUTH) # dining room is south of kitchen
link_bidirectional(diningroom, ballroom, Direction.WEST) # ballroom is west of dining room

kitchen.print_details()
diningroom.print_details()
ballroom.print_details()