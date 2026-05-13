import unittest

# Function to be tested
def add(a, b):
    return a + b

# Test case class
class TestMathOperations(unittest.TestCase):
    
    # Test method
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)  # Check if the result is 5
        
    def test_add_negative(self):
        result = add(-1, 1)
        self.assertEqual(result, 0)  # Check if the result is 0

# Run the tests
if __name__ == '__main__':
    unittest.main()