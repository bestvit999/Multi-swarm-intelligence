import numpy as np
from config import Config as cf

"""
[Reference]
https://www.sfu.ca/~ssurjano/index.html
"""

def calculation(array):#as you want
    test_fn = cf.get_test_fn()
    if test_fn == 'rastrigin':
        return rastrigin(array)
    elif test_fn == 'sphere':
        return sphere(array)
    elif test_fn == 'rosenbrock':
        return rosenbrock(array)
    elif test_fn == 'michalewicz':
        return michalewicz(array)
    else:
        return ackley(array)

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
    
def eggholder(array):
    z = - (array[1] + 47) * np.sin(np.sqrt(abs(array[1] + (array[0]/2) +47))) - array[0] *np.sin(np.sqrt(abs(array[0] - (array[1]+47))))
    return z

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

if __name__ == '__main__':
    a = np.array([2.20, 1.57,])
    print (michalewicz(a))
