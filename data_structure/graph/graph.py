from vertex import Vertex
# 当边的数量庞大时，邻接矩阵是图的一个良好的实现方法, 太稀疏了
# 我们维护一 个包含所有顶点的主列表(master list)，主列表中的每个顶点，再关联一个与自身有边连接的所有 顶点的列表。
# 在实现顶点类的方法里，我们使用字典而不是列表，此时字典中的键(key)对应顶点 标识，而值(value)则可以保存顶点连接边的权重。
# 邻接表实现方法的优点是允许我们高效地表示一个稀疏图。邻接链表还使我们很容易找到某个顶点与其他顶点的所有连接。

class Graph:
    """Graph 类，包含了一个将顶点名称映射到顶点对象的字典。在图 7.4 中这个字典对 象被阴影灰色框所代表
    ，Graph 也提供了向图中添加顶点和将一个顶点与另一个连接起来的方法。 
    getVertices 方法可以返回图中所有顶点的名称。另外我们可以通过实现__iter__方法简化对特定图中 所有顶点对象的遍历。
    这两种方法允许你通过顶点名称或顶点对象本身去遍历图中的顶点
    """

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, id):
        newVertex = Vertex(id)
        self.vertList[id] = newVertex
        self.numVertices += 1
        return newVertex

    def getVertex(self, id):
        if id in self.vertList:
            return self.vertList[id]
        else:
            return None

    def __contains__(self,id):
        return  id in self.vertList
        
    def addEdge(self, id1, id2, weight = 0):
        if id1 not in self.vertList:
            vertex1 = self.addVertex(id1)
        if id2 not in self.vertList:
            vertex2 = self.addVertex(id2)
        self.vertList[id1].addNeighbor(self.vertList[id2], weight)    #单向图


    def getVertices(self):
        return self.vertList.keys()   # 返回一个字典所有的键。keys()

    def __iter__(self):
        return iter(self.vertList.values()) # 返回字典中的所有值。 values()