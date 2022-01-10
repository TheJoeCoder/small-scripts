from enum import Enum, auto

class Direction(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
class Game():
    def __init__(self):
        self.rooms = {}
        self.pointer = (0, 0)
    def getpointer(self):
        return self.pointer
    def getroom(self):
        return self.rooms[self.pointer]
    def getroomfromxy(self, xy):
        return self.rooms[xy]
    def move(self, movement):
        previouspos = self.pointer
        try:
            if movement == Direction.NORTH:
                self.pointer = (self.pointer[0], self.pointer[1] + 1)
            if movement == Direction.SOUTH:
                self.pointer = (self.pointer[0], self.pointer[1] - 1)
            if movement == Direction.EAST:
                self.pointer = (self.pointer[0] + 1, self.pointer[1])
            if movement == Direction.WEST:
                self.pointer = (self.pointer[0] - 1, self.pointer[1])
            if self.getroom() == None:
                self.pointer = previouspos
                return None
            else:
                return self.getroom()
        except KeyError:
            self.pointer = previouspos
            return None
    def canmove(self, movement):
        try:
            newroom = None
            if movement == Direction.NORTH:
                newroom = self.getroomfromxy((self.pointer[0], self.pointer[1] + 1))
            if movement == Direction.SOUTH:
                newroom = self.getroomfromxy((self.pointer[0], self.pointer[1] - 1))
            if movement == Direction.EAST:
                newroom = self.getroomfromxy((self.pointer[0] + 1, self.pointer[1]))
            if movement == Direction.WEST:
                newroom = self.getroomfromxy((self.pointer[0] - 1, self.pointer[1]))
            if newroom == None:
                return False
            else:
                return True
        except KeyError:
            return False
    def addroom(self, xy, room):
        self.rooms[xy] = room
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def getname(self):
        return self.name
    def getdescription(self):
        return self.description