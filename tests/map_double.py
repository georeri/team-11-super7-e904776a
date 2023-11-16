from levelup.map import Map
from levelup.position import Position
from levelup.direction import Direction

class MapDouble (Map):

    STUBBED_X = 3
    STUBBED_Y = 4
    starting_position = Position(0,0)

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        # What should we return here so our character tests will work in isolation?
        if direction == Direction.EAST:
            self.starting_position.x = current_position.x + 1
            self.starting_position.y = current_position.y
        elif direction == Direction.WEST:
            self.starting_position.x = current_position.x - 1
            self.starting_position.y = current_position.y
        elif direction == Direction.NORTH:
            self.starting_position.x = current_position.x
            self.starting_position.y = current_position.y - 1
        elif direction == Direction.SOUTH:
            self.starting_position.x = current_position.x
            self.starting_position.y = current_position.y + 1
        else:
            print("move method takes direction")

        return self.starting_position
