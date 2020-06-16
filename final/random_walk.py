import numpy as np
from config import Config as cf


class RandomWalk():
    def __init__(self):
        """ adaptive learning rate (element-wised) """
        self.vr = np.zeros(shape=cf.get_dimension())
        self.var = np.zeros(shape=cf.get_dimension())
        self.var_t = check_bound(np.random.uniform(low=cf.get_min_domain(), high=cf.get_max_domain(), size=cf.get_dimension()))

    def tweak_normal(self, mean=0.0, stddev=0.05):
        step = np.random.normal(loc=mean, scale=stddev, size=self.var_t.shape)
        return step

    def cal_ada_lr(self):
        """
            beta = 0.999
            var = var_t - var
            vr_t = beta * vr + (1 - beta) * var_t ** 2
        """
        beta = 0.999
        self.var = self.var_t - self.var
        self.vr = beta * self.vr + (1 - beta) * np.power(self.var, 2)
        vr_sqrt = np.sqrt(self.vr)
        return vr_sqrt

def check_bound(array):
    for i in range(len(array)):
        if array[i] > cf.get_max_domain():
            array[i] = cf.get_max_domain()
        elif array[i] < cf.get_min_domain():
            array[i] = cf.get_min_domain()
    return array