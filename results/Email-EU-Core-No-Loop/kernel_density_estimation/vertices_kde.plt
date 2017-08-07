reset
set datafile separator ","

set terminal postscript eps color

set style line 4 linecolor rgb "red"  linewidth 1.000 dashtype solid pointtype 1 pointsize default pointinterval 0

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
set yrange [-0.005625:0.025]
plot "vertex_measures.csv" using 3:(0.005625*rand(0)-0.005625) linestyle 4 notitle ,\
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
set yrange [-2:8]
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

set output "avg_nbr_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:600]
set yrange [-0.003:0.012]
plot "vertex_measures.csv" using 9:(0.003*rand(0)-0.003) linestyle 4 notitle ,\
     "vertex_measures.csv" using 9:1 smooth kdensity linestyle 4 title "Average Neighbor Degree"

set output "avg_nbr_in_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:250]
set yrange [-0.00625:0.025]
plot "vertex_measures.csv" using 10:(0.00625*rand(0)-0.00625) linestyle 4 notitle ,\
     "vertex_measures.csv" using 10:1 smooth kdensity linestyle 4 title "Average Neighbor In-Degree"

set output "avg_nbr_out_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:350]
set yrange [-0.00625:0.025]
plot "vertex_measures.csv" using 11:(0.00625*rand(0)-0.00625) linestyle 4 notitle ,\
     "vertex_measures.csv" using 11:1 smooth kdensity linestyle 4 title "Average Neighbor Out-Degree"

set output "sum_nbr_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:30000]
set yrange [-0.00005:0.0002]
plot "vertex_measures.csv" using 12:(0.00005*rand(0)-0.00005) linestyle 4 notitle ,\
     "vertex_measures.csv" using 12:1 smooth kdensity linestyle 4 title "Sum Neighbor Degree"

set output "sum_nbr_in_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:15000]
set yrange [-0.0001:0.0004]
plot "vertex_measures.csv" using 13:(0.0001*rand(0)-0.0001) linestyle 4 notitle ,\
     "vertex_measures.csv" using 13:1 smooth kdensity linestyle 4 title "Sum Neighbor In-Degree"

set output "sum_nbr_out_deg_vertices.eps"
set title "Kernel Density Estimation\nfor All Vertices"
set xrange[0:15000]
set yrange [-0.0001:0.0004]
plot "vertex_measures.csv" using 14:(0.0001*rand(0)-0.0001) linestyle 4 notitle ,\
     "vertex_measures.csv" using 14:1 smooth kdensity linestyle 4 title "Sum Neighbor Out-Degree"

