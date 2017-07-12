reset
set datafile separator ","

set title "Absolute Triangle Count"

set xlabel "Minimum Threshold"
set xrange [0:0.6]
#set logscale x 2

set ylabel "Count"
set logscale y 10
set format y "%.0e"
set yrange [1:1000000]

set key horizontal
set key outside bottom center
set key height 2


set style line 4 lt rgb "red"  lw 4 pt 7
set style line 5 lt rgb "blue" lw 4 pt 5
set style line 6 lt rgb "green" lw 4 pt 4
set style line 7 lt rgb "purple" lw 4 pt 6

set terminal postscript eps color
set output "absolute_triangle_count.eps"

plot "betweenness_centrality.csv" using 1:(($3/3)+1) with linespoints linestyle 4 title "Betweenness" ,\
     "closeness_centrality.csv"   using 1:(($3/3)+1) with linespoints linestyle 5 title "Closeness" ,\
     "eigenvector_centrality.csv" using 1:(($3/3)+1) with linespoints linestyle 6 title "Eigenvector" ,\
     "pagerank.csv"               using 1:(($3/3)+1) with linespoints linestyle 7 title "PageRank"

