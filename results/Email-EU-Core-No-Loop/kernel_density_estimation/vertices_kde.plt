reset
set datafile separator ","

set terminal postscript eps color

set style line 4 linecolor rgb "red"  linewidth 1.000 dashtype solid pointtype 1 pointsize default pointinterval 0
set style line 5 lt rgb "blue" lw 4

set xlabel "Value"
set ylabel "Density"

#set key outside bottom horizontal center




set output "degree_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:600]
set yrange [-0.003:0.012]
plot "vertex_measures.csv" using 2:(0.003*rand(0)-0.003) linestyle 4 notitle ,\
     "vertex_measures.csv" using 2:1 smooth kdensity linestyle 4 title "Degree"

set output "in_degree_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:600]
set yrange [-0.003:*]
plot "vertex_measures.csv" using 3:(0.003*rand(0)-0.003) linestyle 4 notitle ,\
     "vertex_measures.csv" using 3:1 smooth kdensity linestyle 4 title "In Degree"

set output "out_degree_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:350]
set yrange [-0.005625:0.025]
plot "vertex_measures.csv" using 4:(0.005625*rand(0)-0.005625) linestyle 4 notitle ,\
     "vertex_measures.csv" using 4:1 smooth kdensity linestyle 4 title "Out Degree"

set output "betweenness_centrality_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:0.08]
set yrange [-75:300]
plot "vertex_measures.csv" using 5:(75*rand(0)-75) linestyle 4 notitle ,\
     "vertex_measures.csv" using 5:1 smooth kdensity linestyle 4 title "Betweenness Centrality"

set output "closeness_centrality_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set yrange [-1:8]
set xrange[0:0.6]
plot "vertex_measures.csv" using 6:(2*rand(0)-2) linestyle 4 notitle ,\
     "vertex_measures.csv" using 6:1 smooth kdensity linestyle 4 title "Closeness Centrality"

set output "eigenvector_centrality_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:0.16]
set yrange [-7.5:35]
plot "vertex_measures.csv" using 7:(7.5*rand(0)-7.5) linestyle 4 notitle ,\
     "vertex_measures.csv" using 7:1 smooth kdensity linestyle 4 title "Eigenvector Centrality"

set output "pagerank_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:0.008]
set yrange [-175:700]
plot "vertex_measures.csv" using 8:(175*rand(0)-175) linestyle 4 notitle ,\
     "vertex_measures.csv" using 8:1 smooth kdensity linestyle 4 title "PageRank"

set output "sum_nbr_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:0.008]
set yrange [-175:700]
plot "vertex_measures.csv" using 9:(175*rand(0)-175) linestyle 4 notitle ,\
     "vertex_measures.csv" using 9:1 smooth kdensity linestyle 4 title "Sum Neighbor Degree"

set output "avg_nbr_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:0.008]
set yrange [-175:700]
plot "vertex_measures.csv" using 10:(175*rand(0)-175) linestyle 4 notitle ,\
     "vertex_measures.csv" using 10:1 smooth kdensity linestyle 4 title "Average Neighbor Degree"
