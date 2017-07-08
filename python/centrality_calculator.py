import sys
import argparse
import networkx

from graph_utils import read_graph, write_graph

def main(source_file, destination_file=None, source_type=None, destination_type=None, undirected=False):
	if undirected:
		create_using = networkx.Graph
	else:
		create_using = networkx.DiGraph
	
	sys.stderr.write("Reading Graph...")
	sys.stderr.flush()
	graph = read_graph(source_file, source_type, create_using)
	sys.stderr.write("done.\n")

	sys.stderr.write("Degree...")
	sys.stderr.flush()
	degree = graph.degree()
	networkx.set_node_attributes(graph, "degree", degree)
	sys.stderr.write("done.\n")

	if not undirected:
		sys.stderr.write("In Degree...")
		sys.stderr.flush()
		degree = graph.in_degree()
		networkx.set_node_attributes(graph, "in_degree", degree)
		sys.stderr.write("done.\n")
		
		sys.stderr.write("Out Degree...")
		sys.stderr.flush()
		degree = graph.out_degree()
		networkx.set_node_attributes(graph, "out_degree", degree)
		sys.stderr.write("done.\n")
	
	sys.stderr.write("Page Rank...")
	sys.stderr.flush()
	pagerank = networkx.pagerank(graph)
	networkx.set_node_attributes(graph, "pagerank", pagerank)
	sys.stderr.write("done.\n")
	
	sys.stderr.write("Closeness Centrality...")
	sys.stderr.flush()
	closeness_centrality = networkx.closeness_centrality(graph)
	networkx.set_node_attributes(graph, "closeness_centrality", closeness_centrality)
	sys.stderr.write("done.\n")

	sys.stderr.write("Betweenness Centrality...")
	sys.stderr.flush()
	betweenness_centrality = networkx.betweenness_centrality(graph)
	networkx.set_node_attributes(graph, "betweenness_centrality", betweenness_centrality)
	sys.stderr.write("done.\n")
	
	sys.stderr.write("Eigenvector Centrality...")
	sys.stderr.flush()
	eigenvector_centrality = networkx.eigenvector_centrality(graph)
	networkx.set_node_attributes(graph, "eigenvector_centrality", eigenvector_centrality)
	sys.stderr.write("done.\n")

	if undirected:
		sys.stderr.write("Clustering Coefficent...")
		sys.stderr.flush()
		clustering = networkx.clustering(graph)
		networkx.set_node_attributes(graph, "clustering", clustering)
		sys.stderr.write("done.\n\n")

	
	sys.stderr.write("Writing Graph...")
	sys.stderr.flush()
	if destination_file:
		networkx.write_gml(graph, destination_file)
	else:
		networkx.write_gml(graph, "/dev/stdout")
	sys.stderr.write("done.\n")
	
 
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Centrality Calculator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("source_file",      action="store", type=str, metavar="infile", help="input graph name")
	parser.add_argument("destination_file", action="store", type=str, metavar="outfile", help="output graph name")
	
	parser.add_argument("-u", "--undirected", action="store_true", help="construct an undirected graph, directed by default")
	
	parser.add_argument("-st", "--source-type",      required=False, action="store", type=str, metavar="extension", help="file type")
	parser.add_argument("-dt", "--destination-type", required=False, action="store", type=str, metavar="extension", help="file type")
	
	arguments = vars(parser.parse_args())
	try:
		main(**arguments)
	except RuntimeError as re:
		print >>sys.stderr, re

