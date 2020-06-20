import numpy as np

class Config:
    __PopulationSize = 50 # Population Size
    __MaxDomain = -40 # variable upper limit
    __MinDomain = 40 # variable lower limit
    __Lambda = 1.5 # parameter for Levy flight
    __Lmabda_max = 1.99
    __Lmabda_min = 1.0
    __Pa = 0.1
    __Step_Size = 0.5
    __Dimension = 2 # The number of dimension
    __Trial = 31
    __Iteration = 5000
    __Test_fn = 'ackley'
    __Pa_max = 0.2
    __Pa_min = 0.05
    __Step_Size_max = 1.0
    __Step_Size_min = 0.01

    @classmethod
    def sigmoid(cls, x):
        return 1 / (1 + np.exp(-x)) 

    @classmethod
    def get_dynamic_lambda(cls, current_iter):
        return cls.__Lmabda_min + cls.sigmoid(-10 + (current_iter / cls.__Iteration) * 20) * (cls.__Lmabda_max - cls.__Lmabda_min)
        # return cls.__Lmabda_min + (current_iter / cls.__Iteration) * (cls.__Lmabda_max - cls.__Lmabda_min)

    @classmethod
    def get_dynamic_pa(cls, current_iter):
        """ Pa_iter = Pa_max - (current_iter / total_iter) * (Pa_max - Pa_min) """
        return cls.__Pa_max - (current_iter / cls.__Iteration) * (cls.__Pa_max - cls.__Pa_min)
    
    @classmethod
    def get_dynamic_step_size(cls, current_iter):
        """
        Step_Size_iter = Step_Size_max * exp(c * current_iter)
        c = (1 / total_iter) * ln(Step_Size_min / Step_Size_max)
        """
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

    @classmethod
    def setting_domain_bound(cls, test_fn):
        if test_fn == 'rastrigin':
            cls.set_min_domain(-5.12)
            cls.set_max_domain(5.12)
        elif test_fn == 'sphere':
            cls.set_min_domain(-5.12)
            cls.set_max_domain(5.12)
        elif test_fn == 'rosenbrock':
            cls.set_min_domain(-5.0)
            cls.set_max_domain(10.0)
        elif test_fn == 'michalewicz':
            cls.set_min_domain(.0)
            cls.set_max_domain(np.pi)
        elif test_fn == 'ackley':
            cls.set_min_domain(-32.768)
            cls.set_max_domain(32.768)
        elif test_fn == 'schwefel':
            cls.set_min_domain(-500)
            cls.set_max_domain(500)
        elif test_fn == 'griewank':
            cls.set_min_domain(-600)
            cls.set_max_domain(600)
        elif test_fn == 'sharffer':
            cls.set_min_domain(-100)
            cls.set_max_domain(100)
        elif test_fn == 'bohachevsky':
            cls.set_min_domain(-100)
            cls.set_max_domain(100)
        elif test_fn == 'sumSquares':
            cls.set_min_domain(-5.12)
            cls.set_max_domain(5.12)
        elif test_fn == 'booth':
            cls.set_min_domain(-10)
            cls.set_max_domain(10)
        elif test_fn == 'zakharov':
            cls.set_min_domain(-5)
            cls.set_max_domain(10)
        elif test_fn == 'threeHumpCamel':
            cls.set_min_domain(-5)
            cls.set_max_domain(5)
        elif test_fn == 'deJong':
            cls.set_min_domain(-65.536)
            cls.set_max_domain(65.536)
        elif test_fn == 'beale':
            cls.set_min_domain(-4.5)
            cls.set_max_domain(4.5)
        elif test_fn == 'powell':
            cls.set_min_domain(-4)
            cls.set_max_domain(5)
        else:
            print('error: no function')
            exit()