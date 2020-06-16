REM argv => testFunction; dimension; iteration; runs;

REM ackley
python .\pso.py ackley 2 5000 30
python .\pso.py ackley 10 5000 30
python .\pso.py ackley 20 5000 30
python .\pso.py ackley 30 5000 30

REM Rastrigin
python .\pso.py rastrigin 2 5000 30
python .\pso.py rastrigin 10 5000 30
python .\pso.py rastrigin 20 5000 30
python .\pso.py rastrigin 30 5000 30

REM Sphere
python .\pso.py sphere 2 5000 30
python .\pso.py sphere 10 5000 30
python .\pso.py sphere 20 5000 30
python .\pso.py sphere 30 5000 30

REM Rosenbrock
python .\pso.py rosenbrock 2 5000 30
python .\pso.py rosenbrock 10 5000 30
python .\pso.py rosenbrock 20 5000 30
python .\pso.py rosenbrock 30 5000 30

REM Michalewicz
python .\pso.py michalewicz 2 5000 30
python .\pso.py michalewicz 10 5000 30
python .\pso.py michalewicz 20 5000 30
python .\pso.py michalewicz 30 5000 30