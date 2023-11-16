from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    MIN_ALLOWED = 0
    MAX_ALLOWED = 9
    starting_position = Position(MIN_ALLOWED, MIN_ALLOWED)
    size: Tuple[int, int] = (MAX_ALLOWED, MAX_ALLOWED)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        self.starting_position = Position(self.MIN_ALLOWED, self.MIN_ALLOWED)
        self.positions = []
        for x in range(self.MIN_ALLOWED, self.MAX_ALLOWED + 1):
            self.positions.append([Position(x,y) for y in range(self.MIN_ALLOWED, self.MAX_ALLOWED + 1)])
        self.size = (self.MAX_ALLOWED + 1,self.MAX_ALLOWED + 1)

    def is_position_valid(self, position :Position) -> bool:
        if ((self.MIN_ALLOWED <= position.x <= self.MAX_ALLOWED) and (self.MIN_ALLOWED <= position.y <= self.MAX_ALLOWED)):
            return True
        else:
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
            # print("move method takes direction")
            raise Exception("You somehow managed to pass in an invalid direction. Good job - Nailed it.")
        return self.starting_position
