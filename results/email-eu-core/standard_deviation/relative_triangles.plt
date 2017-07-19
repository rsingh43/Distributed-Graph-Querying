reset
set datafile separator ","

set title "Relative Triangle Count"

set xlabel "+/- Std. Dev. Arround Mean"
set xrange [0.00001:25.0]
set xtics add ("0" 0.00001)
set format x "%g"
set logscale x
xfix(xx) = (xx == 0) ? 0.00001 : xx

set ylabel "Count"
set yrange [0.0001:100]
set ytics add ("0" 0.0001)
set format y "%.3f%%"
set logscale y 10
yfix(yy) = (yy == 0) ? 0.0001 : yy

set key horizontal
set key outside bottom center
set key height 2

set style line 4 lt rgb "red"  lw 4 pt 7
set style line 5 lt rgb "blue" lw 4 pt 5
set style line 6 lt rgb "green" lw 4 pt 4
set style line 7 lt rgb "purple" lw 4 pt 6

set terminal postscript eps color
set output "relative_triangle_count.eps"

plot "betweenness_centrality.csv" using (xfix($1)):(yfix(($3/3)/(347700/3)*100)) with linespoints linestyle 4 title "Betweenness" ,\
     "closeness_centrality.csv"   using (xfix($1)):(yfix(($3/3)/(347700/3)*100)) with linespoints linestyle 5 title "Closeness" ,\
     "eigenvector_centrality.csv" using (xfix($1)):(yfix(($3/3)/(347700/3)*100)) with linespoints linestyle 6 title "Eigenvector" ,\
     "pagerank.csv"               using (xfix($1)):(yfix(($3/3)/(347700/3)*100)) with linespoints linestyle 7 title "PageRank"

