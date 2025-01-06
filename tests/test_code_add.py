import json
import unittest
from functions import add, minus

class TestAddFunction(unittest.TestCase):
    def test_add_cases(self):
        """Test cases for add() function."""
        with open("./tests/test_cases_add.json", "r") as f:
            test_cases = json.load(f)
        
        for case in test_cases:
            a = case["input"]["a"]
            b = case["input"]["b"]
            expected = case["expected"]
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

if __name__ == "__main__":
    unittest.main()
