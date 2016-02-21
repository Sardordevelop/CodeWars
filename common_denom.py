from fractions import gcd

def lcm(lst):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, lst, 1)


def convertFracts(lst):
    result = []
    lcm_ = lcm([x[1] for x in lst])
    for i in range(len(lst)):
        result.append([lcm_/lst[i][1], lcm_])
    return result

a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
c = [x[1] for x in a]
print convertFracts(a)