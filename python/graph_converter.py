import sys, os
import argparse
import networkx
import numpy

from graph_utils import read_graph, write_graph

def main(source_file, destination_file, source_type=None, destination_type=None, undirected=False):

	if undirected:
		create_using = networkx.Graph
	else:
		create_using = networkx.DiGraph
	
	graph = read_graph(source_file, source_type, create_using)
	write_graph(graph, destination_file, destination_type)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Graph Converter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

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
