# assume get_values already covered by unit tests
def get_values():
    f = open('variances.txt')
    return f.readline()


def sqrt(x,iteration=10,convergence=10e-3,round_off=3): # In place of Sqrt, sqrt is preferred according to PEP8 formatting
    """This method determines square root of a non-negative real number using 'Heron's method'

    Args:
        x (float): non-negative real number whose square root is to be determined
        iteration (integer): no. of iterations required for convergence (optional input)
        convergence (float): convergence criteria (optional input)
        round_off (integer): rounding off the output upto decimal places (optional input)

    Returns:
        z (float): square root of x
    """    
    z = 1.0 # This is the initial guess, any arbitrary positive value works
    temp = 0 # placeholder to keep 'z' for checking convergence
    for i in range(iteration):
        z -= (z*z - x) / (2*z)
        # print(z)   # unnecessary print statement within for loop slows down the code significantly, so commenting this line
        if abs(temp-z) <= convergence: # checking whether two subsequent vaues of 'z' is below convergence
            break
        temp = z
    z = round(z,round_off) # rounding of z according to convergence
    print(f"Square root of {x} is {z}") # this print sattement may be commented for a large size data in variances.txt file
    return z


def get_standard_deviation(variance): # it is always better to write function names explicitly
    """standard deviation is the square root of variance

    Args:
        variance (float): non-negative real number whose standard deviation is to be determined

    Returns:
        float: standard deviation
    """  
    standard_deviation = sqrt(variance)  
    return standard_deviation


def get_std_values():
    """This method reads the input values using get_values() function, determines the standard deviation
    and collects them in a list

    Returns:
        standard_deviation (list): standard deviation of the input values
    """    
    standard_deviation = [] # this is an empty list that will store the standard deviation of the input variance
    input_values = get_values() # the variance values of "variances.txt" is stored here
    input_values = input_values.split(',') # we expect the values in the text file is separated by comma
    input_values = [eval(i) for i in input_values] # converting strings to numbers
    for i in input_values: # i is a preferred index in a for loop (followed by j and k)
        standard_deviation = standard_deviation + [get_standard_deviation(i)]

    return standard_deviation


if __name__ == "__main__":
    # testing the code here

    # testing get_values()
    var1 = get_values()
    print(var1)

    # testing sqrt(x)
    var2 = sqrt(144)

    # testing
    var3 = get_std_values()
    print(var3)