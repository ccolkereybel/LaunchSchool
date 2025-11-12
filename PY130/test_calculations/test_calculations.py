import unittest
from calculations import calculate_sum

class TestCalculateSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(5, calculate_sum(3,2))

    def test_negative_numbers(self):
        self.assertEqual(-9, calculate_sum(-5,-4))

    def test_mixed_numbers(self):
        self.assertEqual(3, calculate_sum(-2, 5))


if __name__ == '__main__':
    unittest.main()