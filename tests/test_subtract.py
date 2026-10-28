import unittest

from app import subtract


class SubtractTest(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
