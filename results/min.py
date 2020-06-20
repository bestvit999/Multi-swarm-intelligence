import pandas as pd

algos = ['pso', 'cs', 'ics', 'cs-adaptive']
test_fns = ['ackley', 'rastrigin', 'sphere', 'rosenbrock', 'michalewicz', 'schwefel', 'griewank', 'sumSquares', 'zakharov', 'bohachevsky', 'scharffer', 'booth', 'threeHumpCamel', 'deJong', 'beale', 'powell']
dimensions = [2, 10, 20, 30]

for algo in algos:
    for test_fn in test_fns:
        for dimension in dimensions:
            try:
                df = pd.read_csv('{}/{}-{}/avg-of-30-trial.txt'.format(algo, test_fn, dimension), sep = ' ', header=None, usecols=[1])
                print(algo, test_fn, '{:10.10f}'.format(float(df.min())))
            except:
                pass