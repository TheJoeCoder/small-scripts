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
    
    def set_name(self, name: str) -> None:
        self.name = name
    
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
    
    def move(self, direction: Direction):
        if direction in self.linkedrooms:
            return self.linkedrooms[direction]
        else:
            print("You can't move that way!")
            return self

class Item:
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = "No description given."
    def get_name(self) -> str:
        return self.name
    def set_name(self, name: str) -> None:
        self.name = name
    def get_description(self) -> str:
        return self.description
    def set_description(self, description: str) -> None:
        self.description = description

class Character:
    def __init__(self, char_name, char_description) -> None:
        self.name = char_name
        self.description = char_description
        self.conversation = None
    def describe(self) -> None:
        print(self.name + " is here!")
        print(self.description)
    def talk(self) -> None:
        if self.conversation is not None:
            print("[" + self.name + "]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you.")
    def fight(self, combat_item: Item) -> bool:
        print(self.name + " doesn't want to fight with you.")
        return True
    def set_conversation(self, conversation: str) -> None:
        self.conversation = conversation

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

current_room = kitchen

dave = Character("Dave", "A smelly zombie")
dave.set_conversation("Hallo! I be Dave!")

dave.describe()
dave.talk()

while True:
    print("\n")
    current_room.print_details()
    command = input("> ")
    try:
        current_room = current_room.move(Direction(command.upper()))
    except:
        print("Invalid command")
