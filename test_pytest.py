import functions    # The code to test

def test_sqrt(): # testing the sqrt() function
    assert functions.sqrt(64) == 8 # demonstration for an integer value

def test_sqrt(): # testing the sqrt() function
    assert functions.sqrt(3) == 1.732 # demonstration for a float value

def test_get_standard_deviation(): # testing the get_standard_deviation() function
    assert functions.get_standard_deviation(5) == 2.236

def test_get_std_values(): # testing the get_std_values() function
    assert functions.get_std_values() == [1.0, 1.414, 1.732, 2.0, 2.236, 2.449, 2.646, 2.828, 3.0, 3.162, 3.317, 3.464, 3.606, 3.742, 3.873, 4.0, 4.123, 4.243, 4.359, 4.472]
    # user can modify the variances.txt file to change the input
    # accordingly the assert condition on line no. 13 is to be modified
