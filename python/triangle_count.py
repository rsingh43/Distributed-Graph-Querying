import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

def main(attribute, minimum_filter_value, filter_step, maximum_filter_value, host):
	endpoint = SPARQLWrapper(host)
	
	query = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?node1 paypal:connects ?node2 .
	?node2 paypal:connects ?node3 .
	?node3 paypal:connects ?node1 .
}}
"""
	
	endpoint.setQuery(query)
	endpoint.setReturnFormat(JSON)
	results = endpoint.query().convert()
	total = int(results['results']['bindings'][0]['total']['value'])
	print total

	if attribute:
		query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?node1 paypal:connects ?node2 .
	?node2 paypal:connects ?node3 .
	?node3 paypal:connects ?node1 .
	?node1 paypal:{attribute} ?value1 .
	?node2 paypal:{attribute} ?value2 .
	?node3 paypal:{attribute} ?value3 .
	FILTER(?value1 >= {value}) .
	FILTER(?value2 >= {value}) .
	FILTER(?value3 >= {value}) .
}}
"""
		
		while maximum_filter_value >= minimum_filter_value:
			query = query_pattern.format(attribute=attribute, value=maximum_filter_value)
			endpoint.setQuery(query)
			endpoint.setReturnFormat(JSON)
			results = endpoint.query().convert()
			total = int(results['results']['bindings'][0]['total']['value'])
			print maximum_filter_value, total
			maximum_filter_value -= filter_step

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Triangle Count", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser = argparse.ArgumentParser(description="Triangle Count")

	parser.add_argument("-a", "--attribute", action="store", type=str, metavar="name", help="attribute used for filtering")
	
	parser.add_argument("-m", "--minimum-filter-value", action="store", type=float, default=0.1, metavar="val", help="minimum filtering value")
	parser.add_argument("-M", "--maximum-filter-value", action="store", type=float, default=1.0, metavar="val", help="maximum filtering value")
	parser.add_argument("-s", "--filter-step",          action="store", type=float, default=0.1, metavar="val", help="filtering step value")
	
	parser.add_argument("--host", action="store", type=str, default="http://localhost:6060/ds/query", metavar="hostname", help="SPARQL endpoint")
	
	arguments = vars(parser.parse_args())
	main(**arguments)