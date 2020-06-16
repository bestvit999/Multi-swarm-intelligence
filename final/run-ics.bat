REM argv => testFunction; dimension; iteration; runs;

REM ackley
python .\ics.py ackley 2 5000 30
python .\ics.py ackley 10 5000 30
python .\ics.py ackley 20 5000 30
python .\ics.py ackley 30 5000 30

REM Rastrigin
python .\ics.py rastrigin 2 5000 30
python .\ics.py rastrigin 10 5000 30
python .\ics.py rastrigin 20 5000 30
python .\ics.py rastrigin 30 5000 30

REM Sphere
python .\ics.py sphere 2 5000 30
python .\ics.py sphere 10 5000 30
python .\ics.py sphere 20 5000 30
python .\ics.py sphere 30 5000 30

REM Rosenbrock
python .\ics.py rosenbrock 2 5000 30
python .\ics.py rosenbrock 10 5000 30
python .\ics.py rosenbrock 20 5000 30
python .\ics.py rosenbrock 30 5000 30

REM Michalewicz
python .\ics.py michalewicz 2 5000 30
python .\ics.py michalewicz 10 5000 30
python .\ics.py michalewicz 20 5000 30
python .\ics.py michalewicz 30 5000 30