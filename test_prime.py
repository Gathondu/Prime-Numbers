import unittest

from prime import Prime


class PrimeTest(unittest.TestCase):

    # set up variables that we will use globally
    def setUp(self):
        self.prime = Prime()

    def test_invalid_input(self):
        result = self.prime.primeNumbers("string")
        assertEqual(result, 'Input value should be an Integer', 'Input allows invalid input')

    def test_that_input_should_be_greater_than_1(self):
        result = self.prime.primeNumbers(1)
        self.assertEqual(result, 'Input should be a number greater than 1', 'Input allows incorrect values')

    # Test that the function gives correct output with 2 as input
    # Test that the function gives correct output with 3 as input
    # Test that the function gives correct output with 5 as input
    # Test that the function gives correct output with 16 as input
    # Test that the function gives correct output with 37 as input
    # Test that the function gives correct output with 166 as input
