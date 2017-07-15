reset
set datafile separator ","

set title "Absolute Triangle Count"

set xlabel "Minimum Threshold"
set xrange [0.00001:1.0]
set xtics add ("0" 0.00001)
set format x "%.0g"
set logscale x

set ylabel "Count"
set logscale y 10
set format y "%.0e"
set yrange [1:1000000]

set key horizontal
set key outside bottom center
set key height 2

fix(xx) = (xx == 0) ? 0.00001 : xx

set style line 4 lt rgb "red"  lw 4 pt 7
set style line 5 lt rgb "blue" lw 4 pt 5
set style line 6 lt rgb "green" lw 4 pt 4
set style line 7 lt rgb "purple" lw 4 pt 6

set terminal postscript eps color
set output "absolute_triangle_count.eps"

plot "betweenness_centrality.min.csv" using (fix($1)):(($3/3)+1) with linespoints linestyle 4 title "Betweenness" ,\
     "closeness_centrality.min.csv"   using (fix($1)):(($3/3)+1) with linespoints linestyle 5 title "Closeness" ,\
     "eigenvector_centrality.min.csv" using (fix($1)):(($3/3)+1) with linespoints linestyle 6 title "Eigenvector" ,\
     "pagerank.min.csv"               using (fix($1)):(($3/3)+1) with linespoints linestyle 7 title "PageRank"

