#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
mi = __import__('6-max_integer').max_integer


class TestListToMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_mi(self):
        """ method to test with some examples
        """
        self.assertEqual(mi([1, 3, 5]), 5)
        self.assertEqual(mi([20, 4, 6]), 20)
        self.assertEqual(mi([1, 1, 0, -6]), 1)
        self.assertEqual(mi([50, 70, 90, 80, 90, 10]), 90)
        self.assertEqual(mi("ricardo"), "r")
        self.assertEqual(mi([[5, 0], [4, 20]]), [5, 0])
        self.assertEqual(mi([9]), 9)
        self.assertEqual(mi(""), None)
        self.assertEqual(mi([]), None)
        self.assertEqual(mi(), None)
        with self.assertRaises(TypeError):
            mi(["hello", 1, 2])
