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

if os.path.exists('results/pso/{}-{}'.format(test_fn, dimension)):
    result = open('results/pso/{}-{}/avg-of-{}-trial.txt'.format(test_fn, dimension, trials), 'w+')
else:
    os.makedirs('results/pso/{}-{}'.format(test_fn, dimension))
    result = open('results/pso/{}-{}/avg-of-{}-trial.txt'.format(test_fn, dimension, trials), 'w+')


def main():
    for trial in range(cf.get_trial()):
        np.random.seed(trial)

        result_list = np.zeros(cf.get_iteration())
        pos_list = []
        v_list = []
        pbest_list = []
        gbest = None
        

        """Generate Initial Population"""
        gbest = id.Individual()
        for p in range(cf.get_population_size()):
            pbest_list.append(id.Individual())
            pos_list.append(id.Individual())
            v_list.append(id.Individual())

        """ Main Loop """
        for iteration in range(cf.get_iteration()):
            """ Update Partical position """
            for i in range(cf.get_population_size()):
                # move to new position
                pos_list[i].get_newPos(v_list[i], pbest_list[i], gbest)

                # update fitness
                fitness = fn.calculation(pos_list[i].get_position(), 0)
                pos_list[i].set_fitness(fitness)

                # update pbest & gbest
                if pos_list[i].get_fitness() < pbest_list[i].get_fitness():
                    pbest_list[i].set_position(pos_list[i].get_position())
                    pbest_list[i].set_fitness(pos_list[i].get_fitness())

                if pos_list[i].get_fitness() < gbest.get_fitness():
                    gbest.set_position(pos_list[i].get_position())
                    gbest.set_fitness(pos_list[i].get_fitness())
                
            # print([x.get_fitness() for x in pbest_list])
            # print(gbest.get_fitness())
            sys.stdout.write("\r Trial:%3d , Iteration:%7d, BestFitness:%.4f" % (trial , iteration, gbest.get_fitness()))
            result_list[iteration] += gbest.get_fitness()
    
    """ export avg result"""
    result_list /= cf.get_trial()
    for iteration in range(cf.get_iteration()):
        result.write('{} {}\n'.format(iteration, result_list[iteration]))



if __name__ == '__main__':
    main()