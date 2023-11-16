from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    MIN_ALLOWED = 0
    MAX_ALLOWED = 9
    starting_position = Position(0,0)
    # positions = []
    size: Tuple[int, int] = (10, 10)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        # TODO: implement method here and remove the print statement below
        # print("map constructor method not yet implemented")
        self.starting_position = Position(0,0)
        self.positions = []
        for x in range(0,10):
            self.positions.append([Position(x,y) for y in range(0,10)])
        self.size = (10,10)
        self.size: Tuple[int, int] = (10, 10)

    def is_position_valid(self, position :Position) -> bool:
        # TODO: implement method here and remove the print statement below
        print("is_position_valid method not yet implemented")
        return False        

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        # What should we return here so our character tests will work in isolation?
        if direction == Direction.EAST:
            self.starting_position.x = min(current_position.x + 1, self.MAX_ALLOWED)
            self.starting_position.y = current_position.y
        elif direction == Direction.WEST:
            self.starting_position.x = max(current_position.x - 1, self.MIN_ALLOWED)
            self.starting_position.y = current_position.y
        elif direction == Direction.NORTH:
            self.starting_position.x = current_position.x
            self.starting_position.y = max(current_position.y - 1, self.MIN_ALLOWED)
        elif direction == Direction.SOUTH:
            self.starting_position.x = current_position.x
            self.starting_position.y = min(current_position.y + 1, self.MAX_ALLOWED)
        else:
            print("move method takes direction")

        return self.starting_position
