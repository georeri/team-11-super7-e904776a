from levelup.position import Position
from levelup.direction import Direction
from levelup.map import Map

DEFAULT_CHARACTER_NAME = "Character"
class Character:
    # In python, we don't use getters. So no getPosition or getName for this class
    name = ""
    current_position = Position(0, 0)
    gameMap = Map()
    is_move_called = False
    last_move_direction = None
    is_enter_map_called = False

    # Since python doesn't do method overloading, this is how we support a constructor with optional parameters
    def __init__(self, character_name=DEFAULT_CHARACTER_NAME):
        if character_name.strip() == '':
            self.name = DEFAULT_CHARACTER_NAME
        else:
            self.name = character_name

    def move(self, direction :Direction) -> None:
        self.current_position = self.gameMap.calculate_new_position(self.current_position, direction)
        self.last_move_direction = direction
        self.is_move_called = True
    
    def enter_map(self, gameMap :Map) -> None:
        # TODO: implement method here and remove the print statement below
        self.gameMap = gameMap
        self.gameMap.starting_position = self.current_position
        self.is_enter_map_called = True
        # print("enter_map method not yet implemented")
