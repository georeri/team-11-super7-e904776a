from unittest import TestCase
from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position

class TestMap(TestCase):
    
    # # Remove comments to run this test, which will motivate you to write the production method
    def test_init_creates_positions(self):
        testobj = Map()
        # import pdb
        # pdb.set_trace()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(10, len(testobj.positions))

    # # Remove comments to run this test, which will motivate you to write the production method
    def test_init_creates_positions_with_correct_x_y(self):
        testobj = Map()
        self.assertEqual(3, testobj.positions[3][0].x)
        self.assertEqual(7, testobj.positions[3][7].y)

    # # Remove comments to run this test, which will motivate you to write the production method
    def test_is_position_valid_when_true(self):
        testobj = Map()
        self.assertTrue(testobj.is_position_valid(Position(3,4)))

    # Given the example above, what should these test?
    def test_is_position_valid_when_x_too_small(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(-1,4)))

    def test_is_position_valid_when_x_too_big(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(30,4)))

    def test_is_position_valid_when_y_too_small(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(3,-4)))

    def test_is_position_valid_when_y_too_big(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(3,40)))

    def test_is_position_valid_when_x_and_y_too_big(self):
        testobj = Map()
        self.assertFalse(testobj.is_position_valid(Position(50,60)))

    # # Remove comments to run this test, which will motivate you to write the production method
    def test_calculate_new_position_when_valid_NORTH(self):
        testobj = Map()
        startingPosition = Position(5,5)
        expectedPosition = Position(5,4)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.NORTH)
        self.assertEqual(expectedPosition, actualPosition)

    # Given the example above, what should these test?
    def test_calculate_new_position_when_valid_SOUTH(self):
        testobj = Map()
        startingPosition = Position(2,2)
        expectedPosition = Position(2,3)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.SOUTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_EAST(self):
        testobj = Map()
        startingPosition = Position(6,6)
        expectedPosition = Position(7,6)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.EAST)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_WEST(self):
        testobj = Map()
        startingPosition = Position(2,2)
        expectedPosition = Position(1,2)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.WEST)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_invalid_NORTH(self):
        testobj = Map()
        startingPosition = Position(5,0)
        expectedPosition = Position(5,0)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.NORTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_invalid_SOUTH(self):
        testobj = Map()
        startingPosition = Position(5,9)
        expectedPosition = Position(5,9)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.SOUTH)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_EAST(self):
        testobj = Map()
        startingPosition = Position(9,5)
        expectedPosition = Position(9,5)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.EAST)
        self.assertEqual(expectedPosition, actualPosition)

    def test_calculate_new_position_when_valid_WEST(self):
        testobj = Map()
        startingPosition = Position(0,5)
        expectedPosition = Position(0,5)
        actualPosition = testobj.calculate_new_position(startingPosition, Direction.WEST)
        self.assertEqual(expectedPosition, actualPosition)
