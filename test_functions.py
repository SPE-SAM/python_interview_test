import unittest
import functions  # Import the functions.py module


class TestFunctions(unittest.TestCase):

    def test_get_values(self):
        # Test case 1: File exists with content
        with open('variances_Test.txt', 'w') as f:
            f.write("10\n110\n20\n660")
        self.assertEqual(functions.get_values('variances_Test.txt'),
                         ['10\n', '110\n', '20\n', '660'])

        # Test case 2: File exists but is empty
        with open('variances_Test.txt', 'w'):
            pass
        self.assertEqual(functions.get_values('variances_Test.txt'), [])

    def test_sqrt(self):
        # Test cases for the sqrt() function
        # Test case 1: Check for positive value
        self.assertAlmostEqual(functions.sqrt(25), 5.0)

        # Test case 2: Check for zero
        self.assertAlmostEqual(functions.sqrt(1), 1.0)

        # Test case 3: Check for negative value
        with self.assertRaises(ValueError):
            functions.sqrt(-10)

        # Test case 4: Convergence test with different iterations
        self.assertAlmostEqual(functions.sqrt(
            10.45, convergence=1e-2, round_off=3), 3.233)

    def test_get_std_deviation(self):
        # Test cases for the get_std_deviation() function
        # Test case 1: Check for variance = 10.0
        self.assertAlmostEqual(
            functions.get_std_deviation(10.0), 3.162, places=3)

        # Test case 2: Check for variance = 110.0
        self.assertAlmostEqual(
            functions.get_std_deviation(110.0), 10.488, places=3)

        # Test case 3: Check for variance = 660.0
        self.assertAlmostEqual(
            functions.get_std_deviation(660.0), 25.690, places=3)

    def test_get_std_values(self):
        # Test cases for the get_std_values() function
        # Test case 1: Check for standard deviations
        with open('variances.txt', 'w') as f:
            f.write("10, 20, 50, 60.0")

        expected_stds = [3.162, 4.472, 7.071, 7.746]
        self.assertListEqual(functions.get_std_values(), expected_stds)

        # Test case 2: Invalid characters in 'variances_Test.txt'
        with open('variances.txt', 'w') as f:
            f.write("10, 110.0, A20, 660.0")

        expected_stds = [3.162, 10.488, 25.69]
        self.assertListEqual(functions.get_std_values(), expected_stds)

        # Test case 3: File with empty lines
        with open('variances.txt', 'w') as f:
            f.write("\n20\n\n660\n")

        expected_stds = [4.472, 25.69]
        self.assertListEqual(functions.get_std_values(), expected_stds)

        # Test case 4: Single value in 'variances_Test.txt'
        with open('variances.txt', 'w') as f:
            f.write("10")

        expected_stds = [3.162]
        self.assertListEqual(functions.get_std_values(), expected_stds)


# Run the tests
if __name__ == '__main__':
    unittest.main()
