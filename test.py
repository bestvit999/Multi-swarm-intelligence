import numpy as np
import math
import pandas as pd
from config import Config as cf

def sigmoid(x):
    return 1 / (1 + np.exp(-x)) 

def get_dynamic_lambda(current_iter):
    return 1.0 + sigmoid(-10 + (current_iter / 5000) * 20) * (2.0 - 1.0)

def levy_flight(Lambda):
    #generate step from levy distribution
    sigma1 = np.power((math.gamma(1 + Lambda) * np.sin((np.pi * Lambda) / 2)) \
                      / math.gamma((1 + Lambda) / 2) * Lambda * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
    sigma2 = 1
    u = np.random.normal(0, np.power(sigma1, 2), size=100)
    v = np.random.normal(0, np.power(sigma2, 2), size=100)
    step = u / np.power(np.fabs(v), 1 / Lambda)

    return step    # return np.array (ex. [ 1.37861233 -1.49481199  1.38124823])

w = open('tttt.txt', 'w')
for i in range(5000):
    _lambda = get_dynamic_lambda(i)
    step = levy_flight(_lambda)
    w.write('{} {}\n'.format(i, float(pd.DataFrame(step).std())))
