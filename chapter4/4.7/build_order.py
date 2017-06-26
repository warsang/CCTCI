import unittest

test = unittest.TestCase()

class Node(object):
	
	def __init__(self,name,incoming = None,outgoing = None):
		self.name = name
		self.incoming = incoming
		self.outgoing = outgoing
	

def build_order(projects,dependencies):
	return_list = []
	#Step 1: Build Graph from lists
	graph = dict()
	for element in projects:	
		graph[element] = Node(element)
	for element in dependencies:
		if graph[element[0]].outgoing is None:
			graph[element[0]].outgoing = [graph[element[1]]]
		else:
			graph[element[0]].outgoing.append(graph[element[1]])
		if graph[element[1]].incoming is None:	
			graph[element[1]].incoming = [graph[element[0]]]
		else:
			graph[element[1]].incoming.append(graph[element[0]])
	#Step 2: Find element with no incoming edges
	while len(return_list) != len(projects):
		for name,node in graph.items():
			if (node.incoming is None or len(node.incoming) == 0) and node.name not in return_list:
				return_list.append(node.name)
				#Delete outgoin edges:
				if node.outgoing is not None:
					for out_node in node.outgoing:
						if node in out_node.incoming:
							out_node.incoming.remove(node)
					node.outgoing = None
					break
		

			else:
				continue
	return return_list	

project = ['a','b','c','d','e','f']
dependencies = [('a','d'),('f','b'),('a','b'),('b','d'),('f','a'),('d','c'),('e','f')]
print(build_order(project,dependencies))
