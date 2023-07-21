# assume get_values already covered by unit tests
def get_values():
    f = open('variances.txt')
    return f.readline()


def Sqrt(x):
    z = 1.0
    for i in range(10):
        z -= (z*z - x) / (2*z)
        print(z)
    return z


def get_std(x):
    # standard deviation is the square root of variance
    return Sqrt(x)


def get_std_values():
    stds = []
    vs = get_values()
    for v in vs:
        stds = stds + [get_std(v)]

    return stds
