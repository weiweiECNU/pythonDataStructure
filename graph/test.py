from graph import Graph
from wordletter import build_graph, bfs, traverse

# 图的调用
# g = Graph()
# for i in range(6):
#     g.addVertex( i )

# print(g.getVertices())
# g.addEdge(0,1,5)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)

# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

# 字梯问题 word letter 
g = build_graph("python/data_structure/graph/wordlist.txt")

start = g.getVertex("which")
bfs(g, start)

#print(g.__iter__)
# traverse(g.getVertex('their'))

traverse(g.getVertex('there'))
 