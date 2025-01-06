import json
import unittest
from functions import add, minus

class TestMinusFunction(unittest.TestCase):
    def test_minus_cases(self):
        """Test cases for minus() function."""
        with open("./tests/test_cases_minus.json", "r") as f:
            test_cases = json.load(f)
        
        for case in test_cases:
            a = case["input"]["a"]
            b = case["input"]["b"]
            expected = case["expected"]
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(minus(a, b), expected)


if __name__ == "__main__":
    unittest.main()
