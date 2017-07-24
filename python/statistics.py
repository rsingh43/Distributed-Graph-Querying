import argparse
from SPARQLWrapper import SPARQLWrapper, JSON
from itertools import izip
import numpy
import tabulate

def main(attributes, query_endpoint, tablefmt):
	endpoint = SPARQLWrapper(query_endpoint)

	lines = []
	for attribute in attributes:
		lines.append("    ?vertex paypal:{attribute} ?{attribute} .".format(attribute=attribute))

	query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT *
WHERE {{
{pattern}
}}
"""
	values = []
	query = query_pattern.format(pattern="\n".join(lines))
	print query
	endpoint.setQuery(query)
	endpoint.setReturnFormat(JSON)
	results = endpoint.query().convert()
	for result in results['results']['bindings']:
		row = [float(result[attribute]["value"]) for attribute in attributes]
		values.append(row)

	values = zip(*values)

	table = [["", "Min", "Max", "Mean", "Std. Dev."]]
	for ii,attribute in enumerate(attributes):
		row = [attribute] + [numpy.amin(values[ii]), numpy.amax(values[ii]), numpy.mean(values[ii]), numpy.std(values[ii])]
		table.append(row)

	print tabulate.tabulate(table, headers="firstrow", tablefmt=tablefmt)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Triangle Count", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser = argparse.ArgumentParser(description="Triangle Count")

	parser.add_argument("-a", "--attributes", nargs="+", required=True, type=str, metavar="name", help="attribute used for filtering")
	parser.add_argument("--query-endpoint", action="store", type=str, default="http://localhost:3030/ds/query", metavar="URL", help="SPARQL endpoint")
	parser.add_argument("--tablefmt", action="store", type=str, choices=["plain", "simple", "grid", "fancy_grid", "pipe", "orgtbl", "jira", "psql", "rst", "mediawiki", "moinmoin", "html", "latex", "latex_booktabs", "textile"], default="simple", metavar="fmt", help="tabulate table format")

	
	arguments = vars(parser.parse_args())
	main(**arguments)
