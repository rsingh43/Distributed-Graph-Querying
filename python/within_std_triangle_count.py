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

	stats_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT ?mean ((SUM((?value - ?mean)*(?value - ?mean)))/COUNT(?value) AS ?var)  (MIN(?value) as ?min) (MAX(?value) as ?max)
WHERE {{
	?src paypal:{attribute} ?value .
	{{
		SELECT (AVG(?value) AS ?mean)
		WHERE {{
			?src paypal:{attribute} ?value .
		}}
	}}
}}
GROUP BY ?mean
"""
	query = stats_query_pattern.format(attribute=attribute)
	endpoint.setQuery(query)
	endpoint.setReturnFormat(JSON)
	results = endpoint.query().convert()
	mean = float(results['results']['bindings'][0]['mean']['value'])
	var = float(results['results']['bindings'][0]['var']['value'])
	mm = float(results['results']['bindings'][0]['min']['value'])
	MM = float(results['results']['bindings'][0]['max']['value'])
	st_dev = var ** 0.5

	triple_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	?src paypal:connects ?dst .
	?src paypal:{attribute} ?value1 .
	?dst paypal:{attribute} ?value2 .
	FILTER(?value1 >= {min} && ?value1 <= {max}) .
	FILTER(?value2 >= {min} && ?value2 <= {max}) .
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
	FILTER(?value1 >= {min} && ?value1 <= {max}) .
	FILTER(?value2 >= {min} && ?value2 <= {max}) .
	FILTER(?value3 >= {min} && ?value3 <= {max}) .
}}
"""
	
	for ii in xrange(501):
		filter_value =  0.0001*ii**2
		
		min_val = mean - (filter_value * st_dev)
		max_val = mean + (filter_value * st_dev)
		query = triple_query_pattern.format(attribute=attribute, min=min_val, max=max_val)
		endpoint.setQuery(query)
		endpoint.setReturnFormat(JSON)
		results = endpoint.query().convert()
		triples = int(results['results']['bindings'][0]['total']['value'])
		
		query = triangle_query_pattern.format(attribute=attribute, min=min_val, max=max_val)
		endpoint.setQuery(query)
		endpoint.setReturnFormat(JSON)
		results = endpoint.query().convert()
		triangles = int(results['results']['bindings'][0]['total']['value'])

		if triples == max_triples and triangles == max_triangles:
			for jj in xrange(ii, 501):
				filter_value =  0.0001*jj**2
				print "{},{},{}".format(filter_value, triples, triangles)
			break
		else:
			print "{},{},{}".format(filter_value, triples, triangles)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Triangle Count: Within Standard Deviation", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser = argparse.ArgumentParser(description="Triangle Count")

	parser.add_argument("-a", "--attribute", required=True, type=str, metavar="name", help="attribute used for filtering")
	
	parser.add_argument("--query-endpoint", type=str, default="http://localhost:3030/ds/query", metavar="URL", help="SPARQL endpoint")
	
	arguments = vars(parser.parse_args())
	main(**arguments)

