set term svg
set ylabel 'fitness'
set xlabel 'iteration'
set grid
set key outside
set xrange [10:5000]

do for [func in "ackley rastrigin sphere rosenbrock michalewicz schwefel griewank sharffer bohachevsky sumSquares booth zakharov threeHumpCamel deJong beale powell"]{
    do for [dimension in "2 10 20 30"]{
        set output 'figure/final/'.func.'-'.dimension.'.svg'
        set title func
        plot for [dataset in "cs ics cs-adaptive pso"] dataset."/".func."-".dimension."/avg-of-30-trial.txt" u 1:2 w lp pi 200 title dataset
    }
}