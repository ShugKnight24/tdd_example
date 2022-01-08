from fizzbuzz import convert_to_fizzbuzz
import unittest

# Test cases written top -> down
class TestFizzbuzz(unittest.TestCase):

	def test_smallest_not_divisible_by_three_or_five(self):
		self.assertEqual('1', convert_to_fizzbuzz(1))

	def test_largest_not_divisible_by_three_or_five(self):
		self.assertEqual('98', convert_to_fizzbuzz(98))

	def test_smallest_divisible_by_three(self):
		self.assertEqual('Fizz', convert_to_fizzbuzz(3))

	def test_largest_divisible_by_three(self):
		self.assertEqual('Fizz', convert_to_fizzbuzz(99))

	def test_smallest_divisible_by_five(self):
		self.assertEqual('Buzz', convert_to_fizzbuzz(5))

	def test_largest_divisible_by_five(self):
		self.assertEqual('Buzz', convert_to_fizzbuzz(100))

	def test_smallest_divisible_by_three_and_five(self):
		self.assertEqual('Buzz', convert_to_fizzbuzz(15))

	def test_largest_divisible_by_three_and_five(self):
		self.assertEqual('Buzz', convert_to_fizzbuzz(90))

	def test_if_input_contains_a_digit_three_then_we_expect_fizz(self):
		self.assertEqual('Fizz', convert_to_fizzbuzz(13))

	def test_if_input_contains_a_digit_five_then_we_expect_buzz(self):
		self.assertEqual('Buzz', convert_to_fizzbuzz(52))

	def test_if_input_contains_a_digit_three_and_a_five_then_we_expect_fizzbuzz(self):
		self.assertEqual('FizzBuzz', convert_to_fizzbuzz(53))

	def test_if_input_contains_a_digit_a_five_and_is_multiple_of_three_then_we_expect_fizzbuzz(self):
		self.assertEqual('FizzBuzz', convert_to_fizzbuzz(51))

if __name__ == '__main__':
	unittest.main()  # pragma: no cover
