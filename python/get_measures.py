import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

def main(attributes, query_endpoint):
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
	table = [["weight"] + attributes]
	query = query_pattern.format(pattern="\n".join(lines))
	#print query
	endpoint.setQuery(query)
	endpoint.setReturnFormat(JSON)
	results = endpoint.query().convert()
	for result in results['results']['bindings']:
		row = [str(1.0/len(results['results']['bindings']))] + [result[attribute]["value"] for attribute in attributes]
		table.append(row)
	
	print "\n".join(",".join(row) for row in table)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Get Vertex Measures", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser = argparse.ArgumentParser(description="Triangle Count")

	parser.add_argument("-a", "--attributes", nargs="+", required=True, type=str, metavar="name", help="attribute used for filtering")
	parser.add_argument("--query-endpoint", action="store", type=str, default="http://localhost:3030/ds/query", metavar="URL", help="SPARQL endpoint")
	
	arguments = vars(parser.parse_args())
	main(**arguments)
