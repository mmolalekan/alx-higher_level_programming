#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """using assertEqual"""
        # Test case 1: Valid list with positive integers
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

        # Test case 2: Valid list with negative integers
        self.assertEqual(max_integer([-5, -2, -7, -3, -1]), -1)

        # Test case 3: Valid list with both positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

        # Test case 4: Valid list with duplicate integers
        self.assertEqual(max_integer([5, 2, 3, 5, 1]), 5)

        # Test case 5: Valid list with a single integer
        self.assertEqual(max_integer([10]), 10)

        # Test case 6: Empty list
        self.assertEqual(max_integer([]), None)

        # Test case 7: List with all zeros
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

        # Test case 10: List with floating-point numbers
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 2.5]), 3.1)

        # Test case 9: List with non-integer elements
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_max_integer_raise(self):
        # Test case 8: List with mix of integers and other types
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3, 4])
