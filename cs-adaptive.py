import numpy as np
import individual as id
import function as fn
import sys
import os
import csv
from config import Config as cf

test_fn = sys.argv[1]
dimension = int(sys.argv[2])
iterations = int(sys.argv[3])
trials = int(sys.argv[4])

cf.set_test_fn(test_fn)
cf.setting_domain_bound(test_fn)
cf.set_dimension(dimension)
cf.set_iteration(iterations)
cf.set_trial(trials)


if os.path.exists('results/cs-adaptive/{}-{}'.format(test_fn, dimension)):
    result = open('results/cs-adaptive/{}-{}/avg-of-{}-trial.txt'.format(test_fn, dimension, trials), 'w+')
else:
    os.makedirs('results/cs-adaptive/{}-{}'.format(test_fn, dimension))
    result = open('results/cs-adaptive/{}-{}/avg-of-{}-trial.txt'.format(test_fn, dimension, trials), 'w+')

def main():
    result_list = np.zeros(cf.get_iteration())
    for trial in range(cf.get_trial()):
        # np.random.seed(trial)
        np.random.seed()
        
        cs_list = []
        """Generate Initial Population"""
        for p in range(cf.get_population_size()):
            cs_list.append(id.Individual())

        """Sort List"""
        cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())

        """Find Initial Best"""
        BestPosition = cs_list[0].get_position()
        BestFitness = fn.calculation(cs_list[0].get_position(),0)

        """↓↓↓Main Loop↓↓↓"""
        for iteration in range(cf.get_iteration()):

            """Generate New Solutions"""
            for i in range(len(cs_list)):
                cs_list[i].get_cuckoo_dynamic_adaptive(iteration)
                cs_list[i].set_fitness(fn.calculation(cs_list[i].get_position(),iteration))

                """random choice (say j)"""
                j = np.random.randint(low=0, high=cf.get_population_size())
                while j == i: #random id[say j] ≠ i
                    j = np.random.randint(0, cf.get_population_size())

                # for minimize problem
                if(cs_list[i].get_fitness() < cs_list[j].get_fitness()):
                    cs_list[j].set_position(cs_list[i].get_position())
                    cs_list[j].set_fitness(cs_list[i].get_fitness())

            """Sort (to Keep Best)"""
            cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())

            """Abandon Solutions (exclude the best)"""
            for a in range(1,len(cs_list)):
                r = np.random.rand()
                if(r < cf.get_Pa()):
                    cs_list[a].abandon_dynamic(iteration)
                    cs_list[a].set_fitness(fn.calculation(cs_list[a].get_position(),iteration))

            """Sort to Find the Best"""
            cs_list = sorted(cs_list, key=lambda ID: ID.get_fitness())

            if cs_list[0].get_fitness() < BestFitness:
                BestFitness = cs_list[0].get_fitness()
                BestPosition = cs_list[0].get_position()

            sys.stdout.write("\r Trial:%3d , Iteration:%7d, BestFitness:%.10f" % (trial , iteration, BestFitness))
            result_list[iteration] += BestFitness

    """ export avg result"""
    result_list /= cf.get_trial()
    for iteration in range(cf.get_iteration()):
        result.write('{} {}\n'.format(iteration, result_list[iteration]))

if __name__ == '__main__':
    main()
    