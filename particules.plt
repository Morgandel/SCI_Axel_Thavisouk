set terminal pngcairo size 1280,800
set output 'collisions.png'                      # y-axis label

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

set title "Courbe du nombres de colisions selon la taille d'une grille"                # plot title
set xlabel 'Tours'                       # x-axis label
set ylabel 'Collisions'

plot '50x50.data' using 1:2 with lines title '50x50', '100x100.data' using 1:2 with lines title '100x100', '150x150.data' using 1:2 with lines title '150x150', '200x200.data' using 1:2 with lines title '200x200'
