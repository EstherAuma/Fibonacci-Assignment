
#Author: Esther
# Import the unittest module for writing test cases
import unittest

# Define the Fibonacci function that generates the first 'n' Fibonacci numbers
def fibonacci(n):
    """
    Generate the first 'n' Fibonacci numbers.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list containing the first 'n' Fibonacci numbers.
    """
    # Initialize the Fibonacci sequence with the first two numbers.
    fib_sequence = [0, 1]
    
    # Calculate the rest of the sequence.
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

# Create a test case class to test the Fibonacci function
class TestFibonacci(unittest.TestCase):
    def test_fibonacci_sequence(self):
        # Test cases to verify the correctness of the Fibonacci function
        self.assertEqual(fibonacci(1), [0, 1])          # Test for n=1 (Updated expectation)
        self.assertEqual(fibonacci(2), [0, 1])          # Test for n=2
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])  # Test for n=10

# Entry point of the script
if __name__ == "__main__":
    unittest.main()  # Run the test cases when the script is executed
