import sys
import argparse
import csv
import networkx
from RDFWriter import RDFWriter

from graph_utils import read_graph

def print_message(message, verbose, min_level):
	if verbose >= min_level:
		sys.stderr.write(message)
		sys.stderr.flush()

def main(input_filename, output_filename=None, undirected=False, append_attributes=False, filters=None, verbose=0):

	print_message("Reading {}...".format(input_filename), verbose, 1)
	if undirected:
		graph = read_graph(input_filename, networkx.Graph())
	else:
		graph = read_graph(input_filename, networkx.DiGraph())
	print_message("done.\n", verbose, 1)
	
	
	print_message("Extracting attributes...", verbose, 1)
	measures = set()
	for vertex,attributes in graph.nodes_iter(data=True):
		measures.update(attributes.iterkeys())
	print_message("done.\n", verbose, 1)

	parser = argparse.ArgumentParser()
	for measure in measures:
		if measure != "id" and measure != "label":
			flag = "--min-{}".format(measure)
			help_text = "filter with minimum {}".format(measure.replace("_", " "))
			parser.add_argument(flag, type=float, metavar="val", help=help_text)
			
			flag = "--max-{}".format(measure)
			help_text = "filter with  maximum {}".format(measure.replace("_", " "))
			parser.add_argument(flag, type=float, metavar="val", help=help_text)

	args = parser.parse_args(filters)
	filters_dict = vars(args)
	filters_dict = {key:value for key,value in filters_dict.iteritems() if value}

	if filters_dict:
		filters_used = ["  {}:{}\n".format(key,value) for key,value in filters_dict.iteritems()]
		print_message("Using Filters:\n" + "".join(filters_used), verbose, 2)
		print_message("Filtering vertices...", verbose, 1)
		print_message("\n", verbose, 3)
		for vertex,attributes in graph.nodes_iter(data=True):
			for name,value in attributes.iteritems():
				key = "min_{}".format(name)
				if key in filters_dict:
					if value < filters_dict[key]:
						graph.remove_node(vertex)
						print_message("  {} {}\n".format(key, vertex), verbose, 3)
						break
				
				key = "max_{}".format(name)
				if key in filters_dict:
					if value > filters_dict[key]:
						graph.remove_node(vertex)
						print_message("  {} {}\n".format(key, vertex), verbose, 3)
						break
		print_message("done.\n", verbose, 1)	

	if not output_filename:
		output_filename = "/dev/stdout"
	
	writer = RDFWriter()
	writer.write(graph, output_filename, append_attributes)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Graph to RDF Converter", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument("input_filename",  action="store", metavar="infile",  help="input graph name")
	parser.add_argument("output_filename", action="store", metavar="outfile", help="output graph name, standard out by default")
	parser.add_argument("-u", "--undirected", action="store_true", help="construct an undirected graph, directed by default")
	parser.add_argument("-a", "--append_attributes", action="store_true", help="write graph attributes to RDF file")
	parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
	
	args, filters = parser.parse_known_args()
	arguments = vars(args)
	arguments["filters"] = filters
	try:
		main(**arguments)
	except RuntimeError as re:
		print >>sys.stderr, re
	
 
