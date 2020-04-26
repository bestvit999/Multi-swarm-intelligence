import numpy as np
import math
from config import Config as cf
import function as fn
import random

def levy_flight(Lambda):
    #generate step from levy distribution
    sigma1 = np.power((math.gamma(1 + Lambda) * np.sin((np.pi * Lambda) / 2)) \
                      / math.gamma((1 + Lambda) / 2) * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
    sigma2 = 1
    u = np.random.normal(0, np.power(sigma1, 2), size=cf.get_dimension())
    v = np.random.normal(0, np.power(sigma2, 2), size=cf.get_dimension())
    step = u / np.power(np.fabs(v), 1 / Lambda)

    return step    # return np.array (ex. [ 1.37861233 -1.49481199  1.38124823])


class Individual:
    def __init__(self):
        self.__position = np.random.rand(cf.get_dimension()) * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()
        self.__fitness = fn.calculation(self.__position,0) # iteration = 0

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_fitness(self):
        return self.__fitness

    def set_fitness(self, fitness):
        self.__fitness = fitness

    def abandon(self):
        # abandon some variables
        for i in range(len(self.__position)):
            p = np.random.rand()
            if p < cf.get_Pa():
                self.__position[i] = np.random.rand() * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()

    def abandon_dynamic(self, current_iter):
        # abandon some variables
        for i in range(len(self.__position)):
            p = np.random.rand()
            if p < cf.get_dynamic_pa(current_iter):
                self.__position[i] = np.random.rand() * (cf.get_max_domain() - cf.get_min_domain())  + cf.get_min_domain()

    def get_cuckoo(self):

        step_size = cf.get_stepsize() * levy_flight(cf.get_lambda())

        # Update position
        self.__position = self.__position + step_size

        # Simple Boundary Rule
        for i in range(len(self.__position)):
            if self.__position[i] > cf.get_max_domain():
                self.__position[i] = cf.get_max_domain()
            if self.__position[i] < cf.get_min_domain():
                self.__position[i] = cf.get_min_domain()

    def get_cuckoo_dynamic(self, current_iter):

        step_size = cf.get_dynamic_step_size(current_iter) * levy_flight(cf.get_lambda())

        # Update position
        self.__position = self.__position + step_size

        # Simple Boundary Rule
        for i in range(len(self.__position)):
            if self.__position[i] > cf.get_max_domain():
                self.__position[i] = cf.get_max_domain()
            if self.__position[i] < cf.get_min_domain():
                self.__position[i] = cf.get_min_domain()

    def move(self, target):
        self.__position = self.__position + np.random.rand() * (target - self.__position)

    def get_velocity(self, x_old, p_best, g_best):
        """ v_new = w * v_old + r1 * rho1 * (pb - x_old) + r2 * rho2 * (gb - x_old) """
        w = .25
        rho1 = .25
        rho2 = .25
        r1 = random.random()
        r2 = random.random()
        self.__position = w * self.get_position() + r1 * rho2 * (p_best.get_position() - x_old.__position) + r2 * rho2 * (g_best.get_position() - x_old.__position)

    def get_newPos(self, v_new):
        """ x_new = x_old + v_new """
        self.__position = self.__position + v_new.get_position()

    def print_info(self,i):
        print("id:","{0:3d}".format(i),
              "|| fitness:",str(self.__fitness).rjust(14," "),
              "|| position:",np.round(self.__position,decimals=4))


if __name__ == '__main__':
    print(levy_flight(cf.get_lambda()))

