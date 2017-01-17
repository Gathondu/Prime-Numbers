import unittest

from prime import Prime


class PrimeTest(unittest.TestCase):

    # set up variables that we will use globally
    def setUp(self):
        self.prime = Prime()

    def test_invalid_input_throws_TypeError(self):
        with self.assertRaises(TypeError):
            prime.checkString("string")

    def test_floats_are_rounded_to_nearest_whole_numbers(self):
        result = prime.roundFloat('5.6')
        self.assertEqual(result, 6, "Round function returns invalid output")

    def test_that_input_is_a_number_greater_than_1(self):
        result = prime.getInput(1)
        self.assertEqual(result, 'Input should be a number greter than 1', 'Input allows incorrect values')

    def test_input_less_than_2_throws_ValueError(self):
        with self.assertRaises(ValueError):
            prime.get_input(1)

    # Test that the function gives correct output with 2 as input
    # Test that the function gives correct output with 3 as input
    # Test that the function gives correct output with 5 as input
    # Test that the function gives correct output with 16 as input
    # Test that the function gives correct output with 37 as input
    # Test that the function gives correct output with 166 as input
