'''
Created on July 5th, 2017

@author: Rina Singh
'''
import sys

class RDFWriter(object):
	def __init__(self):
		pass
	
	def write(self, graph, filename, data=False):
		with open(filename, "w") as fp:
			for src, dst in graph.edges_iter():
				subject = "<http://paypal.com/user_{}>".format(src)
				predicate = "<http://paypal.com/connects>"
				object = "<http://paypal.com/user_{}>".format(dst)
				print >>fp, "{} {} {} .".format(subject, predicate, object)
			
			if data:
				for vertex,attributes in graph.nodes_iter(data=True):
					subject = "<http://paypal.com/user_{}>".format(vertex)

					for key,value in attributes.iteritems():
						predicate = "<http://paypal.com/{}>".format(key)

						if type(value) is int:
							object = "\"{}\"^^<http://www.w3.org/2001/XMLSchema#integer>".format(value)
						elif type(value) is float:
							object = "\"{}\"^^<http://www.w3.org/2001/XMLSchema#float>".format(value)
						elif type(value) is str: 
							object = "\"{}\"^^<http://www.w3.org/2001/XMLSchema#string>".format(value)
						elif type(value) is unicode: 
							object = "\"{}\"^^<http://www.w3.org/2001/XMLSchema#string>".format(value)
						else:
							print >>sys.stderr, "Unexpected attribute value type ({}:{}:{}).".format(key, value, type(value))	
							object = "\"{}\"^^<http://www.w3.org/2001/XMLSchema#string>".format(value)

						print >>fp, "{} {} {} .".format(subject, predicate, object)
