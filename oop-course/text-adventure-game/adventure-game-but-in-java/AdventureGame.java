import java.util.HashMap;

public class AdventureGame {
    enum Direction {
        NORTH,
        EAST,
        SOUTH,
        WEST;

        public Direction opposite() {
            if (this == Direction.NORTH) return Direction.SOUTH;
            else if (this == Direction.EAST) return Direction.WEST;
            else if (this == Direction.SOUTH) return Direction.NORTH;
            else if (this == Direction.WEST) return Direction.EAST;
            else return null;
        }
    }
    class Room {
        private String name;
        private String description;
        private HashMap<Direction, Room> linkedrooms;
        public Room(String name) {
            this.name = name;
        }
    }

    public static void main(String[] args) {

    }
}