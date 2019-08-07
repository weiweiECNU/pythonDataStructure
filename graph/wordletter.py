#from graph import Graph
#from vertex import Vertex

from pythonds.graphs import Graph, Vertex 
from pythonds.basic import Queue

def build_graph( wordlist ):
    """
    
    假设我们有非常多的桶,每个桶外都贴有一个四个字母的 单词标签，并且标签上有且仅有一个字母被‘ _’(通配符)所代替。
    例如，考虑图 7.6,我们就可能 会将一个桶贴上“ pop_”， 当我们处理我们的列表中的每个词，都将其与每个桶比较，使用“_” 作为一个通配符,
    那么“pope” 和“ pops” 都与“ pop_”匹配。每次我们找到一个匹配的桶,我 们把单词放在桶里。
    一旦我们把所有单词都放在适当的桶里，我们便知道，同一个桶里的所有单词 都是相互连接的。

       我们可以通过使用一个字典来实现我们刚刚描述的方案。我们刚刚提到的桶上 的标签在我们的字典中作为 key，键值 value 是标签对应的单词列表。
    一旦我们创建了字典我们就 可以生成图。
    
    原因：
    我们为这个 问题准备的 4 个字母的单词列表足足有 5110 个单词那么长。如果我们要使用一个邻接矩阵存储， 矩阵会共有 5110*5110=26112100 个格子。 
    由 buildGraph 函数构建出来的图只有 53286 条边， 所以矩阵将只有 0.20%的格子被填充了
    这个图的确是非常稀疏的。

 
    """

    d = {} # 存桶的 dict
    g = Graph()
    words = open( wordlist,"r" )
    # create buckets of words that differ by one letter
    for lines in words:
        word = lines[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_"+ word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(graph, start):
    """广度优先搜索(BFS) Breadth first search
    从起始顶点 s 开始，此时 s 的颜色被设置为灰色，代表它现在已经被 发现了，另外两个参数——距离和父顶点，对于起始节点 s 初始设置为了 0 和 None。
    随后，起始 节点会被加入到一个队列中，下一步便是系统地探索队首顶点。
    这个过程通过迭代(遍历)队首顶 点的邻接列表来完成，每检查邻接表中的一个顶点，便会维护这个顶点的颜色参量，
    如果颜色是白 色的，就说明这个节点尚未被探索，也就会按下述四步操作:

1、 新的未探索的顶点 nbr，标记为灰色;
2、 nbr 的父顶点被设置为当前节点 currentVert; 
3、 nbr 的距离被设置为当前节点的距离加一;
4、 nbr 被加入队尾，这一操作使得直到 nbr 在当前顶点的邻接列表中的所有顶点被搜索完后，才 能够进行下一层次的探索操作。
    
    
    观察到，当 while 循环被执行时，图的顶点集合|V|中的每个顶点最多被访问一次(也可以从每一个顶点 在被发现和加入队列之前都是白色的得出相同的结论)，
    因而 while 循环拥有 O(V)的复杂度。 另外，对于嵌套在 while 语句中的 for 语句，其对于图的边集|E|中的每一条边至多会被执行一 次。
    这是因为每个顶点只会最多被出队一次，而对于从顶点 u 到顶点 v 的边，只有当顶点 u 出队
    的时候我们才会检查，所以每条边最多被检查一次，因此这个循环的复杂度是 O(E)。这两个循环 的时间复杂度加起来，也就是 O(V+E)。
    
    执行 BFS 只是整个过程中的一部分，找到连接从起始顶点到目标顶点的路径是另一部 分。最坏的情况的从起始顶点到目标顶点就是一条长链，
    在这种情况下遍历所有的顶点的复杂度就 是 O(V)。正常情况下的复杂度是小于|V|的基数的，但我们仍然把 O(V)作为其时间复杂度。"""

    start.setDistance(0)
    start.setPred = None
    vertexToSearch = Queue()
    vertexToSearch.enqueue(start)

    while (vertexToSearch.size() > 0):
        currentVert = vertexToSearch.dequeue()        
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == "white"):
                nbr.setColor("gray")
                nbr.setPred(currentVert)
                nbr.setDistance(currentVert.getDistance() + 1)
                vertexToSearch.enqueue(nbr)
        
        currentVert.setColor("black")

def traverse(y):
    """展示了如何去通过父节点链接来打印出整个词梯。"""
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())






