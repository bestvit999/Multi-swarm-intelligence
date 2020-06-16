import numpy as np
import random
from config import Config as cf
import function as f
import random_walk
import sys

""" argv """

""" config """
cf.set_domain_bound('rastrigin')
cf.set_test_fn('rastrigin')
cf.set_dimension(30)
cf.set_iteration(5000)
cf.set_population_size(50)
epsilon = 1e-07
lr_max = 1.
lr_min = 0.01
lr_t = lr_max
decay_rate = (lr_max - lr_min) / cf.get_iteration()

""" init """
pop = [random_walk.RandomWalk() for i in range(cf.get_population_size())]
best = pop[0]

""" Main Loop """
for iteration in range(cf.get_iteration()):
    lr_t -= decay_rate
    for i in range(cf.get_population_size()):
        #A. calculate momentum
        
        #B. calculate adaptive learning rate
        vr_t = pop[i].cal_ada_lr()

        step = pop[i].tweak_normal(stddev=0.001)

        tweak = pop[i].var_t + lr_t * step / (vr_t + epsilon) + lr_t * (best.var_t - pop[i].var_t) * random.random()

        if f.calculation(tweak) < f.calculation(pop[i].var_t):# or random.random() < 0.001:
            pop[i].var_t = tweak

        if f.calculation(pop[i].var_t) < f.calculation(best.var_t):
            best.var_t = pop[i].var_t

    print('{} {}'.format(iteration, f.calculation(best.var_t), ))