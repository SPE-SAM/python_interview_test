import os

#Default file name is variances.txt for testing file is edited with different values
def get_values(file_name=None):
    # If file name is none or empty input file will be varaince.txt
    if file_name is None or file_name.strip() == '':
        file_name = 'variances.txt'

    # Check for file existence and path
    if os.path.isfile(file_name):
        with open(file_name) as f:
            return f.readlines()
    else:
        raise FileNotFoundError(f"File '{file_name}' not found")


def sqrt(x, convergence=1e-3, round_off=3):
    if x < 0:
        raise ValueError('Input is less than zero')
    else:
        z = 1.0
    temp = 0
    max_iterations = 10

# Max_iteration will be 10 if not conveged solution will check up to 100
# Heros/babylonial method for root finding
    while max_iterations <= 100:
        for i in range(max_iterations):
            z -= (z * z - x) / (2 * z)
            if abs(temp - z) <= convergence:
                break
            temp = z
        else:  # Executed if the loop completes without encountering a 'break'
            max_iterations *= 2
            continue
        break

    if max_iterations > 100:
        print("Warning: The function did not converge within 100 iterations.")

    z = round(z, round_off)
    return z


def get_std_deviation(variance):
    # standard deviation is the square root of variance
    std_deviation = sqrt(variance)
    return std_deviation


def get_std_values():
    stds = []
    vs = get_values()
    all_numbers = []
    file_name = 'variances.txt'
    for v in vs:
        try:
            #Remove any comma , space or new line just take all numbers in a file
            # Remove any non number values like B30,V20 etc
            numbers = [float(num) for num in v.replace(
                ',', ' ').split() if num.strip().replace('.', '').isdigit()]
            all_numbers.extend(numbers)
        except ValueError:
            print(
                f"Warning: Invalid value '{v.strip()}' in '{file_name}'. This will be ignored.")

    for i in all_numbers:
        stds.append(get_std_deviation(i))

    return stds
