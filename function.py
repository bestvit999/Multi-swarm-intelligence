import numpy as np
from config import Config as cf

"""
[Reference]
https://www.sfu.ca/~ssurjano/index.html
"""

def calculation(array, t):#as you want
    test_fn = cf.get_test_fn()
    if test_fn == 'ackley':
        return ackley(array)
    elif test_fn == 'rastrigin':
        return rastrigin(array)
    elif test_fn == 'sphere':
        return sphere(array)
    elif test_fn == 'rosenbrock':
        return rosenbrock(array)
    elif test_fn == 'michalewicz':
        return michalewicz(array)
    elif test_fn == 'schwefel':
        return schwefel(array)
    elif test_fn == 'griewank':
        return griewank(array)
    elif test_fn == 'scharffer':
        return scharffer(array)
    elif test_fn == 'bohachevsky':
        return bohachevsky(array)
    elif test_fn == 'sumSquares':
        return sumSquares(array)
    elif test_fn == 'booth':
        return booth(array)
    elif test_fn == 'zakharov':
        return zakharov(array)
    elif test_fn == 'threeHumpCamel':
        return threeHumpCamel(array)
    elif test_fn == 'deJong':
        return deJong(array)
    elif test_fn == 'beale':
        return beale(array)
    elif test_fn == 'powell':
        return powell(array)
    else:
        print('error')
        exit()

"""Benchmark Functions"""
def ackley(array):
    a = 20
    b = 0.2
    c = 2 * np.pi
    term1 = 0
    term2 = 0
    for x in array:
        term1 += pow(x, 2)
        term2 += np.cos(c * x)
    term1 = -a * np.exp(-b * np.sqrt(term1 / len(array)))
    term2 = -np.exp(term2 / len(array))
    return term1 + term2 + a + np.exp(1)

def rosenbrock(array):
    fitness = 0
    d = len(array)
    for i in range(d-1):
        fitness += 100 * np.power(array[i+1] - np.power(array[i],2), 2) + np.power(array[i] - 1, 2)
    return fitness

def sphere(array):
    fitness = 0
    for i in range(len(array)):
        fitness = fitness + array[i]**2
    return fitness

def rastrigin(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x**2 - 10 * np.cos(2 * np.pi * x)
    fitness = 10.0 * len(array) + sum
    return fitness

def schwefel(array):
    sum = 0
    fitness = 0
    for x in array:
        sum = sum + x * np.sin(np.sqrt(np.abs(x)))
    fitness = 418.9829 * len(array) - sum
    return fitness

def michalewicz(array):#for the number of Dimension is 2
    ans = 0
    for i, x in enumerate(array):
        ans -= np.sin(x) * np.power(np.sin(((i + 1) * x ** 2) / np.pi), 20)
    return ans

def griewank(array):
	part1 = 0
	for i in range(len(array)):
		part1 += array[i]**2
		part2 = 1
	for i in range(len(array)):
		part2 *= np.cos(float(array[i]) / np.sqrt(i+1))
	return 1 + (float(part1)/4000.0) - float(part2)

def scharffer(array):
    if len(array) != 2:
        print('error: sharffer function only 2d')
        exit()
    top = np.sin(array[0] ** 2 - array[1] ** 2) ** 2 - 0.5
    down = (1 + 0.001 * (array[0] ** 2 + array[1] ** 2)) ** 2
    return 0.5 + top / down

def bohachevsky(array):
    if len(array) != 2:
        print('error: bohachevsky function only 2d')
        exit()
    return array[0]**2 + 2*array[1]**2 - 0.3 * np.cos(3 * np.pi * array[0]) \
        - 0.4 * np.cos(4 * np.pi * array[1]) + 0.7

def sumSquares(array):
    ans = 0.0
    for i, xi in enumerate(array):
        ans += (i+1) * xi ** 2
    return ans

def booth(array):
    if len(array) != 2:
        print('error: booth function only 2d')
        exit()
    return (array[0] + 2 * array[1] - 7) **2 + (2 * array[0] + array[1] - 5) **2

def zakharov(array):
    term1 = 0.0
    term2 = 0.0
    term3 = 0.0
    for i, xi in enumerate(array):
        term1 += xi ** 2
        term2 += 0.5 * (i+1) * xi
        term3 += 0.5 * (i+1) * xi
    return term1 + term2 ** 2 + term3 ** 4

def threeHumpCamel(array):
    if len(array) != 2:
        print('error: booth function only 2d')
        exit()
    return 2 * array[0] ** 2 - 1.05 * array[0] ** 4 + array[0] ** 6 / 6 + array[0] * array[1] + array[1] ** 2

def deJong(array):
    if len(array) != 2:
        print('error: deJong function only 2d')
        exit()
    ans = 0.0
    for i in range(-2, 2):
        for j in range(-2, 2):
            ans += (5 * (i + 2) + j + 3 + (array[0] - 16 * j) ** 6 + (array[1] - 16 * i) ** 6) ** -1
    return (0.002 + ans) ** -1

def beale(array):
    if len(array) != 2:
        print('error: beale function only 2d')
        exit()
    term1 = (1.5 - array[0] + array[0] * array[1]) ** 2
    term2 = (2.25 - array[0] + array[0] * array[1] ** 2) ** 2
    term3 = (2.625 - array[0] + array[0] * array[1] ** 3) ** 2
    return term1 + term2 + term3

def powell(array):
    d = int(len(array) / 4)
    ans = 0.0
    for i in range(d):
        ans += (array[4*i-3] + 10 * array[4*i-2]) ** 2 + \
                5 * (array[4*i-1] + array[4*i]) ** 2 + \
                (array[4*i-2] + 2 * array[4*i-1]) ** 4 + \
                10 * (array[4*i-3] + array[4*i]) ** 4
    return ans

if __name__ == '__main__':
    a = np.array([0., 0., 0., 0., 0.,]).astype('float32')
    print(powell(a))
