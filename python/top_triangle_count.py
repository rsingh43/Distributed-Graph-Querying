import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

def main(attribute, query_endpoint, update_endpoint):
	query_endpoint = SPARQLWrapper(query_endpoint)
	update_endpoint = SPARQLWrapper(update_endpoint)
	
	if attribute:
		update_query_pattern = """
DROP SILENT GRAPH <graph:top-k>;
CREATE GRAPH <graph:top-k>;

PREFIX paypal: <http://paypal.com/>

INSERT {{
	GRAPH <graph:top-k> {{
		?src paypal:connects ?dst
	}}
}}
WHERE {{
	{{
		SELECT ?src ?dst
		WHERE {{
			?src paypal:connects ?dst .
			?src paypal:{attribute} ?value .
		}}
		ORDER BY DESC(?value)
		LIMIT {limit}
	}}
	{{
		SELECT ?src ?dst
		WHERE {{
			?dst paypal:connects ?src .
			?dst paypal:{attribute} ?value .
		}}
		ORDER BY DESC(?value)
		LIMIT {limit}
	}}
}}
"""	
		triple_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	GRAPH <graph:top-k> {{
		?src paypal:connects ?dst .
	}}
}}
"""

		triangle_query_pattern = """
PREFIX paypal: <http://paypal.com/>
SELECT (COUNT(*) AS ?total)
WHERE {{
	GRAPH <graph:top-k> {{
		?node1 paypal:connects ?node2 .
		?node2 paypal:connects ?node3 .
		?node3 paypal:connects ?node1 .
	}}
}}
"""
		
		#while maximum_filter_value >= minimum_filter_value:
		for limit in xrange(0, 100000, 250):
			query = update_query_pattern.format(attribute=attribute, limit=limit)
			update_endpoint.setQuery(query)
			update_endpoint.setReturnFormat(JSON)
			results = update_endpoint.query().convert()

			query = triple_query_pattern.format()
			query_endpoint.setQuery(query)
			query_endpoint.setReturnFormat(JSON)
			results = query_endpoint.query().convert()
			triples = int(results['results']['bindings'][0]['total']['value'])
			
			query = triangle_query_pattern.format()
			query_endpoint.setQuery(query)
			query_endpoint.setReturnFormat(JSON)
			results = query_endpoint.query().convert()
			triangles = int(results['results']['bindings'][0]['total']['value'])
			
			print "{},{},{}".format(limit, triples, triangles)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Triangle Count", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser = argparse.ArgumentParser(description="Triangle Count")

	parser.add_argument("-a", "--attribute", required=True, type=str, metavar="name", help="attribute used for filtering")
	
	parser.add_argument("--query-endpoint", type=str, default="http://localhost:3030/ds/query", metavar="URL", help="SPARQL endpoint")
	parser.add_argument("--update-endpoint", type=str, default="http://localhost:3030/ds/update", metavar="URL", help="SPARQL endpoint")
	
	arguments = vars(parser.parse_args())
	main(**arguments)

