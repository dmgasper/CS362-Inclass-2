import unittest
import Fibonacci

class TestFibonacci(unittest.TestCase):
	def test_first_value(self):
		result = Fibonacci.sequence(0)
		self.assertEqual(result, 1)
		
	def test_fifth_value(self):
		result = Fibonacci.sequence(4)
		self.assertEqual(result, 5)
		
	def test_tenth_value(self):
		result = Fibonacci.sequence(9)
		self.assertEqual(result, 55)
		
if __name__ == '__main__':
	unittest.main()
