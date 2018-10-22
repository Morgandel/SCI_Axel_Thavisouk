set terminal pngcairo size 1280,800
set output 'fish_shark.png'
set title "Courbe d'évolution du nombre de poissons par rapport aux requins"                    # plot title
set xlabel 'Poissons'                       # x-axis label
set ylabel 'Requins'                          # y-axis label

#set size ratio 0.5
set grid

# key/legend
set key top right
set key box
#set key right top
set key bmargin

#set nokey     # no key

# arrow
set arrow from 1,1 to 5,1

plot 'poisson.data' using 2:3 with lines title 'Poisson'

set output 'evolution.png'
set title "Courbe d'évolution du nombre de poissons et de requins"                # plot title
set xlabel 'Tours'                       # x-axis label
set ylabel 'Poissons'
set y2label 'Requins'                          # y-axis label

set yrange [0:15000]
set y2range [0:3200]
set y2tics nomirror
set ytics nomirror

plot 'poisson.data' using 1:2 with lines title 'Poisson' axes x1y1, 'poisson.data' using 1:3 with lines title 'Requin' axes x1y2
