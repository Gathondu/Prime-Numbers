import unittest

from prime import Prime


class PrimeTest(unittest.TestCase):

    # set up variables that we will use globally
    def setUp(self):
        self.prime = Prime()

    def test_invalid_input(self):
        result = self.prime.primeNumbers("string")
        self.assertEqual(result, 'Input value should be an Integer', 'Input allows invalid input')

    def test_that_input_should_be_greater_than_1(self):
        result = self.prime.primeNumbers(1)
        self.assertEqual(result, 'Input should be a number greater than 1', 'Input allows incorrect values')

    def test_that_float_inputs_are_rounded_to_next_whole_number(self):
        result = self.prime.primeNumbers(36.7)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 'Floats give incorrect output')

    def test_function_gives_correct_output_with_2(self):
        result = self.prime.primeNumbers(2)
        self.assertEqual(result, [2], 'Incorrect output')

    def test_function_gives_correct_output_with_3(self):
        result = self.prime.primeNumbers(3)
        self.assertEqual(result, [2, 3], 'Incorrect output')

    def test_function_gives_correct_output_with_15(self):
        result = self.prime.primeNumbers(15)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13], 'Incorrect output')

    def test_function_gives_correct_output_with_60(self):
        result = self.prime.primeNumbers(60)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59], 'Incorrect output')

    def test_function_gives_correct_output_with_20(self):
        result = self.prime.primeNumbers(20)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19], 'Incorrect output')

    def test_function_gives_correct_output_with_10(self):
        result = self.prime.primeNumbers(10)
        self.assertEqual(result, [2, 3, 5, 7], 'Incorrect output')

    def test_function_gives_correct_output_with_float(self):
        result = self.prime.primeNumbers(18.6)
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19], 'Incorrect output')

# if __name__ == "__main__":
#     unittest.main()
