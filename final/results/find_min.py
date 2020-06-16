import numpy as np
import pandas as pd

algorithm = ['cs', 'ics', 'pso']
test_fn = ['ackley', 'michalewicz', 'rastrigin', 'rosenbrock', 'sphere']
dimension = ['2','10','20','30']

for algo in algorithm:
    for fn in test_fn:
        for d in dimension:
            df = pd.read_csv('{}/{}-{}/avg-of-30-trial.txt'.format(algo, fn, d),sep=' ', header=None, usecols=[1])
            print(algo, fn, d, float(df.min()))