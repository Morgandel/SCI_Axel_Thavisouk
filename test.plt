set term unknown
plot 'poisson.data' u 1:3  #collect information on our data
FACTOR=0.2248
set y2range [FACTOR*GPVAL_Y_MIN : FACTOR*GPVAL_Y_MAX]
set y2tics nomirror
set ytics nomirror
set terminal pngcairo size 1280,800
set output 'evolution.png'
plot 'poisson.data' using 1:2 with lines title 'Poisson' axes x1y1, 'poisson.data' using 1:3 with lines title 'Requin' axes x1y2
