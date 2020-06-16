import numpy as np

class Config:
    __PopulationSize = 50 # Population Size
    __MaxDomain = -40 # variable upper limit
    __MinDomain = 40 # variable lower limit
    __Lambda = 1.5 # parameter for Levy flight
    __Pa = 0.1
    __Step_Size = 0.5
    __Dimension = 2 # The number of dimension
    __Trial = 31
    __Iteration = 5000
    __Test_fn = 'ackley'
    __Pa_max = 0.2
    __Pa_min = 0.05
    __Step_Size_max = 1.0
    __Step_Size_min = 0.25

    @classmethod
    def set_domain_bound(cls, test_fn):
        if test_fn == 'rastrigin':
            cls.set_min_domain(-5.12)
            cls.set_max_domain(5.12)
        elif test_fn == 'sphere':
            cls.set_min_domain(-5.12)
            cls.set_max_domain(5.12)
        elif test_fn == 'rosenbrock':
            cls.set_min_domain(-2.048)
            cls.set_max_domain(2.048)
        elif test_fn == 'michalewicz':
            cls.set_min_domain(.0)
            cls.set_max_domain(np.pi)
        elif test_fn == 'ackley':
            cls.set_min_domain(-32.768)
            cls.set_max_domain(32.768)
        else:
            cls.set_min_domain(-40)
            cls.set_max_domain(40)

    @classmethod
    def get_dynamic_pa(cls, current_iter):
        """ ICS """
        return cls.__Pa_max - (current_iter / cls.__Iteration) * (cls.__Pa_max - cls.__Pa_min)
    
    @classmethod
    def get_dynamic_step_size(cls, current_iter):
        """ ICS """
        c = (1 / cls.__Iteration) * np.log(cls.__Step_Size_min / cls.__Step_Size_max)
        return cls.__Step_Size_max * np.exp(c * current_iter)
    
    @classmethod
    def get_test_fn(cls):
        return cls.__Test_fn

    @classmethod
    def set_test_fn(cls, _test_fn):
        cls.__Test_fn = _test_fn

    @classmethod
    def get_population_size(cls):
        return cls.__PopulationSize

    @classmethod
    def set_population_size(cls, pop_size):
        cls.__PopulationSize = pop_size

    @classmethod
    def get_Pa(cls):
        return cls.__Pa

    @classmethod
    def get_iteration(cls):
        return cls.__Iteration
    
    @classmethod
    def set_iteration(cls, _iteration):
        cls.__Iteration = _iteration

    @classmethod
    def get_trial(cls):
        return cls.__Trial

    @classmethod
    def set_trial(cls, _trial):
        cls.__Trial = _trial

    @classmethod
    def get_dimension(cls):
        return cls.__Dimension
    
    @classmethod
    def set_dimension(cls, _dimension):
        cls.__Dimension = _dimension

    @classmethod
    def get_max_domain(cls):
        return cls.__MaxDomain

    @classmethod
    def set_max_domain(cls, _max_domain):
        cls.__MaxDomain = _max_domain

    @classmethod
    def get_min_domain(cls):
        return cls.__MinDomain

    @classmethod
    def set_min_domain(cls, _min_domain):
        cls.__MinDomain = _min_domain

    @classmethod
    def get_lambda(cls):
        return cls.__Lambda

    @classmethod
    def set_lambda(cls, _lambda):
        cls.__Lambda = _lambda

    @classmethod
    def get_stepsize(cls):
        return cls.__Step_Size