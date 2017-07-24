import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

def main(attribute, query_endpoint):
	endpoint = SPARQLWrapper(query_endpoint)
	
	triple_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?src paypal:connects ?dst .
}}
"""
	query = triple_query_pattern.format(attribute=attribute)
	endpoint.setQuery(query)
	endpoint.setReturnFormat(JSON)
	results = endpoint.query().convert()
	max_triples = int(results['results']['bindings'][0]['total']['value'])
	
	
	triangle_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?node1 paypal:connects ?node2 .
	?node2 paypal:connects ?node3 .
	?node3 paypal:connects ?node1 .
}}
"""
	query = triangle_query_pattern.format(attribute=attribute)
	endpoint.setQuery(query)
	endpoint.setReturnFormat(JSON)
	results = endpoint.query().convert()
	max_triangles = int(results['results']['bindings'][0]['total']['value'])


	triple_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?src paypal:connects ?dst .
	?src paypal:{attribute} ?value1 .
	?dst paypal:{attribute} ?value2 .
	FILTER(?value1 <= {value}) .
	FILTER(?value2 <= {value}) .
}}
"""

	triangle_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?node1 paypal:connects ?node2 .
	?node2 paypal:connects ?node3 .
	?node3 paypal:connects ?node1 .
	?node1 paypal:{attribute} ?value1 .
	?node2 paypal:{attribute} ?value2 .
	?node3 paypal:{attribute} ?value3 .
	FILTER(?value1 <= {value}) .
	FILTER(?value2 <= {value}) .
	FILTER(?value3 <= {value}) .
}}
"""
	
	for ii in xrange(101):
		filter_value =  0.0001*ii**2

		query = triple_query_pattern.format(attribute=attribute, value=filter_value)
		endpoint.setQuery(query)
		endpoint.setReturnFormat(JSON)
		results = endpoint.query().convert()
		triples = int(results['results']['bindings'][0]['total']['value'])
		
		query = triangle_query_pattern.format(attribute=attribute, value=filter_value)
		endpoint.setQuery(query)
		endpoint.setReturnFormat(JSON)
		results = endpoint.query().convert()
		triangles = int(results['results']['bindings'][0]['total']['value'])
	
		if triples == max_triples and triangles == max_triangles:
			for jj in xrange(ii, 101):
				filter_value =  0.0001*jj**2
				print "{},{},{}".format(filter_value, triples, triangles)
			break
		else:
			print "{},{},{}".format(filter_value, triples, triangles)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Triangle Count: Maximum Threshold", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser = argparse.ArgumentParser(description="Triangle Count")

	parser.add_argument("-a", "--attribute", required=True, type=str, metavar="name", help="attribute used for filtering")
	
	parser.add_argument("--query-endpoint", type=str, default="http://localhost:3030/ds/query", metavar="URL", help="SPARQL endpoint")
	
	arguments = vars(parser.parse_args())
	main(**arguments)
