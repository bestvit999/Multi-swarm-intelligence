set term svg size 600, 400
set ylabel 'fitness'
set xlabel 'iteration'
set grid
set key outside
set xrange [10:5000]

do for [func in "ackley rastrigin sphere rosenbrock michalewicz schwefel griewank sumSquares zakharov"]{
    do for [dimension in "2 10 20 30"]{
        set output 'figure/final/'.func.'-'.dimension.'.svg'
        set title func.'-'.dimension
        plot for [dataset in "cs ics cs-adaptive pso"] dataset."/".func."-".dimension."/avg-of-30-trial.txt" u 1:2 w lp pi 200 title dataset
    }
}

do for [func in "bohachevsky scharffer booth threeHumpCamel deJong beale"]{
    do for [dimension in "2"]{
        set output 'figure/final/'.func.'-'.dimension.'.svg'
        set title func.'-'.dimension
        plot for [dataset in "cs ics cs-adaptive pso"] dataset."/".func."-".dimension."/avg-of-30-trial.txt" u 1:2 w lp pi 200 title dataset
    }
}

do for [func in "powell"]{
    do for [dimension in "10 20 30"]{
        set output 'figure/final/'.func.'-'.dimension.'.svg'
        set title func.'-'.dimension
        plot for [dataset in "cs ics cs-adaptive pso"] dataset."/".func."-".dimension."/avg-of-30-trial.txt" u 1:2 w lp pi 200 title dataset
    }
}