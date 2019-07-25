from pythonds import Graph

class dfsGraph(Graph):
    """更一般的深度优先搜索更容易实现。它的目标是尽可能深地搜索，连接图中尽可 能多的顶点以及仅在必要时建立分支。
    在深度优先搜索中建立不止一个树也是有可能的。当深度优先搜索算法建立一组树时，我们称 之为深度优先森林。
    深度优 先搜索会使用两个附加的 Vertex 类的实例变量。这两个新的实例变量是“发现时间”和“ 结束时 间”。
    “发现时间”记录某个顶点第一次出现前算法的操作步数。“完成时间”则是某个顶点被标 记为黑色之前算法的操作步数。
    
    
   
    
    """
    def __init__(self):
        super.__init__()
        self.time = 0
    
    def dfs(self):
        """ dfs 算法在图中每个白色节点迭代调用 dfsVisit来遍历图中的所有顶点
        for aVertex in self 遍历一个图类的实例中所有的 顶点"""
        for vertex in self:
            vertex.setColor("white")
            vertex.setPred(-1)
        for vertex in self:
            if vertex.getColor() == "white":
                self.dfsVisit(vertex)

    def dfsVisit(self, startVertex):
        """dfsvisit 方法以一个叫做 的单一顶点开始并尽可能深地探索所有相邻白色顶 点。
        如果你仔细观察 的代码并将其与广度优先搜索进行比较，你应当注意到 dfsvisit 算法除了在内部循环的最后一行外与 bfs 几乎相同。 
        dfsvisit 递归调用自身以继续对更深层次的 探索，而 bfs通过将顶点添加到一个队列中以便后续探索。
        需要注意的是，在  bfs使用队列的地 方， dfs使用的是栈。你虽然在代码中看不见栈的形式，但是它暗含在 dfs 的递归调 用中。"""
        startVertex.setColor = "gray"
        self.time += 1
        startVertex.setDiscovery(self.time)
        for neighbourVertex in startVertex.getConnections():
            if neighbourVertex.getColor() == "white":
                neighbourVertex.setPred(startVertex)
                self.dfsVisit(neighbourVertex)
        
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish( self.time )

#深度优先搜索的一般运行时间如下。 dfs中的循环都以𝑂（𝑉）运行，不计算dfsvisit中发生的情况，因为它们对图中的每个顶点执行一次。 
# 在dfsvisit中，循环对当前顶点的邻接列表中的每个边执行一次。 由于dfsvisit仅在顶点为白色时递归调用，因此对于图中的每个边或𝑂（𝐸），循环将执行最多一次。 
# 因此，深度优先搜索的总时间是𝑂（𝑉+𝐸）。