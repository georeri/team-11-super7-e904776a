from unittest import TestCase
from levelup.position import Position


class TestPositionInitWithXY(TestCase):
    def test_init(self):
        Pos_object = Position(3,4)  # Create a new position

        assert Pos_object.x == 3 and Pos_object.y == 4  # Assert that the x and y values are correct
        
if __name__ == "__main__":
    unittest.main()