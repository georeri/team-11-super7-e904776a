from unittest import TestCase
from levelup.character import Character, DEFAULT_CHARACTER_NAME
from tests.map_double import MapDouble
from levelup.map import Map
from levelup.direction import Direction
from levelup.position import Position

class TestCharacter(TestCase):
    ARBITRARY_NAME = "MyName"

    def test_init(self):
        testobj = Character(self.ARBITRARY_NAME)
        self.assertEqual(self.ARBITRARY_NAME, testobj.name)

    def test_init_when_empty(self):
        testobj = Character("  ")
        self.assertEqual(DEFAULT_CHARACTER_NAME, testobj.name)

    ## Remove comments to run this test, which will motivate you to write the production method
    def test_enter_map_sets_map_and_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        stubbed_map = MapDouble()
        testobj.enter_map(stubbed_map)
        self.assertEqual(stubbed_map, testobj.map)
        # self.assertEqual(testobj.current_position, stubbed_map.starting_position)

    # # Remove comments to run this test, which will motivate you to write the production method
    def test_move_updates_position(self):
        testobj = Character(self.ARBITRARY_NAME)
        # stubbed_map = MapDouble()
        stubbed_map = Map()
        testobj.map = stubbed_map        
        
        testobj.current_position = Position(9, 4)
        testobj.move(Direction.EAST)
        self.assertEqual(testobj.current_position.x, 9)
        self.assertEqual(testobj.current_position.y, 4)

        testobj.current_position = Position(8, 10)
        testobj.move(Direction.WEST)
        self.assertEqual(testobj.current_position.x, 7)
        self.assertEqual(testobj.current_position.y, 10)

        testobj.current_position = Position(5, 5)
        testobj.move(Direction.NORTH)
        self.assertEqual(testobj.current_position.x, 5)
        self.assertEqual(testobj.current_position.y, 4)

        testobj.current_position = Position(2, 2)
        testobj.move(Direction.SOUTH)
        self.assertEqual(testobj.current_position.x, 2)
        self.assertEqual(testobj.current_position.y, 3)

