graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'Z': set()}


def dfs(graph, start, finish):

	path = []
	white  = graph.keys()
	black = []
	stack = [(start,[start])]

	while stack:
		node, path = stack.pop(0)
		if node in white:
			black.append(node)
			for x in graph[node] - set(black):
				if x == finish:
					yield path + [x]
				else:
					stack.append( (x, path + [x]))
			white.remove(node)

def dfs_path(graph, start, finish):

	if finish not in graph.keys():
		return None

	if start == finish:
		return None
    
	try:
		generator = dfs(graph, start, finish)
		return next(generator)

	except StopIteration:
		return list(generator)


print dfs_path(graph, 'A', 'Z')

import random
import string



def random_graph_gen(n):
	from random import randint
	rand_graph = {}
	nodes = list( ''.join(random.choice(string.ascii_uppercase) for _ in range(n)))
	for x in nodes:
		m = randint(1,n)
		rand_graph[x] = set([nodes[i] for i in list(random.sample(xrange(n), m))])
	return rand_graph




#print dfs_path(rand_graph, rand_graph.keys()[1], rand_graph.keys()[2])


