reset
set datafile separator ","

set title "Absolute Triple Count"

set xlabel "Minimum Threshold"
set xrange [0.00001:1.0]
set xtics add ("0" 0.00001)
set format x "%.0g"
set logscale x
xfix(xx) = (xx == 0) ? 0.00001 : xx

set ylabel "Count"
set yrange [0.1:1000000]
set ytics add ("0" 0.1)
set format y "%.0e"
set logscale y 10
yfix(yy) = (yy == 0) ? 0.1 : yy

set key horizontal
set key outside bottom center
set key height 2


#set style line 1 lt rgb "red"    lw 4 pt 1
#set style line 2 lt rgb "blue"   lw 4 pt 2
#set style line 3 lt rgb "green"  lw 4 pt 3
#set style line 4 lt rgb "purple" lw 4 pt 4
#set style line 5 lt rgb "brown"  lw 4 pt 5
#set style line 6 lt rgb "orange" lw 4 pt 6
#set style line 7 lt rgb "cyan" lw 4 pt 7

set terminal postscript eps color
set output "absolute_triple_count.eps"

plot "betweenness_centrality.min.csv"   using (xfix($1)):(yfix($2)) with linespoints linestyle 1 title "Betweenness" ,\
     "closeness_centrality.min.csv"     using (xfix($1)):(yfix($2)) with linespoints linestyle 2 title "Closeness" ,\
     "eigenvector_centrality.min.csv"   using (xfix($1)):(yfix($2)) with linespoints linestyle 3 title "Eigenvector" ,\
     "pagerank.min.csv"                 using (xfix($1)):(yfix($2)) with linespoints linestyle 4 title "PageRank" ,\
     "norm_avg_nbr_degree.min.csv"      using (xfix($1)):(yfix($2)) with linespoints linestyle 5 title "Avg. Nbr. Degree" ,\
     "norm_avg_nbr_in_degree.min.csv"   using (xfix($1)):(yfix($2)) with linespoints linestyle 6 title "Avg. Nbr. In Degree" ,\
     "norm_avg_nbr_out_degree.min.csv"  using (xfix($1)):(yfix($2)) with linespoints linestyle 7 title "Avg. Nbr. Out Degree" ,\
     "norm_sum_nbr_degree.min.csv"      using (xfix($1)):(yfix($2)) with linespoints linestyle 8 title "Sum Nbr. Degree" ,\
     "norm_sum_nbr_in_degree.min.csv"   using (xfix($1)):(yfix($2)) with linespoints linestyle 9 title "Sum Nbr. In Degree" ,\
     "norm_sum_nbr_out_degree.min.csv"  using (xfix($1)):(yfix($2)) with linespoints linestyle 10 title "Sum Nbr. Out Degree"
