"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_int_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, 7)

    def test_string_list(self):
        self.assertEqual(max_integer("David"), 'v')

    def test_one_element_list(self):
        self.assertEqual(max_integer([2]), 2)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 2.6, 3.7, 4.8]), 4.8)

    def test_unordered_list(self):
        self.assertEqual(max_integer([10, 23, 13, 54, 100, 99, 74]), 100)

    def test_negative_list(self):
        self.assertEqual(max_integer([-5, -3, -9, -7, -2, -4]), -2)

    def test_first_in_list(self):
        self.assertEqual(max_integer([6.5, 2.6, 3.7, 4.8]), 6.5)

if __name__ == '__main__':
    unittest.main()
