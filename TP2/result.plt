#set terminal pngcairo size 1920,1480
#set output 'resultats.png'

set title 'Comparaison du score obtenu et des meilleurs'                    # plot title
set xlabel 'Tours'                       # x-axis label
set ylabel 'Nombre'                          # y-axis label

#set size ratio 0.5
set grid

# key/legend
set key top right
set key box
set key left bottom
set key bmargin

#set nokey     # no key

# arrow
set arrow from 1,1 to 5,1

plot 'poisson.data' using 1:2 with lines title 'Poisson', 'poisson.data' using 1:3 with lines title 'Requin'
plot 'poisson.data' using 2:3 with lines title 'Poisson'
