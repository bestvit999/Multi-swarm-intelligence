set term svg
set output 'ackley-2.svg'
set yrange [0:0.2]
p 'cs/ackley-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/ackley-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/ackley-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'ackley-10.svg'
unset yrange
p 'cs/ackley-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/ackley-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/ackley-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'ackley-20.svg'
unset yrange
p 'cs/ackley-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/ackley-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/ackley-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'ackley-30.svg'
unset yrange
p 'cs/ackley-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/ackley-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/ackley-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'michalewicz-2.svg'
set yrange [-2.45:-2.44]
p 'cs/michalewicz-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/michalewicz-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/michalewicz-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'michalewicz-10.svg'
unset yrange
p 'cs/michalewicz-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/michalewicz-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/michalewicz-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'michalewicz-20.svg'
unset yrange
p 'cs/michalewicz-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/michalewicz-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/michalewicz-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'michalewicz-30.svg'
unset yrange
p 'cs/michalewicz-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/michalewicz-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/michalewicz-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rastrigin-2.svg'
set yrange [0:0.25]
p 'cs/rastrigin-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rastrigin-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rastrigin-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rastrigin-10.svg'
unset yrange
p 'cs/rastrigin-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rastrigin-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rastrigin-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rastrigin-20.svg'
unset yrange
p 'cs/rastrigin-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rastrigin-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rastrigin-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rastrigin-30.svg'
unset yrange
p 'cs/rastrigin-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rastrigin-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rastrigin-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rosenbrock-2.svg'
set yrange [0:0.4]
p 'cs/rosenbrock-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rosenbrock-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rosenbrock-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rosenbrock-10.svg'
unset yrange
p 'cs/rosenbrock-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rosenbrock-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rosenbrock-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rosenbrock-20.svg'
unset yrange
p 'cs/rosenbrock-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rosenbrock-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rosenbrock-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'rosenbrock-30.svg'
unset yrange
p 'cs/rosenbrock-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/rosenbrock-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/rosenbrock-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'sphere-2.svg'
set yrange [0:0.001]
p 'cs/sphere-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/sphere-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/sphere-2/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'sphere-10.svg'
unset yrange
p 'cs/sphere-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/sphere-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/sphere-10/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'sphere-20.svg'
unset yrange
p 'cs/sphere-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/sphere-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/sphere-20/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'

set term svg
set output 'sphere-30.svg'
unset yrange
p 'cs/sphere-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'cs', \
'ics/sphere-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'ics', \
'pso/sphere-30/avg-of-30-trial.txt' u 1:2 w linespoints pi 100 title 'pso'