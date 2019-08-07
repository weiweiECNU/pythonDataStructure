import sys
class Vertex:
    """Vertex 则描绘了图表中顶点的信息。
    每一个 Vertex 使用一个字典来记录顶点与顶点间的连接关系和每条连 接边的权重，这个字典被称作 connectionTo(self. connectionTo)。
    构造函数(__init___)简单地初始化了(一般为字符串的)id 和 connectionTo 字典。 
    addNeighbor 方法被用来添加从一个顶点到另一个顶点的连接。
    getConnections 方法用以返回以 connectionTo 字典中的实例变量所表示的邻接表中的所有顶点。
    getWeight 方法可以通过一个参数返 回顶点与顶点之间的边的权重。"""

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize # 距离
        self.pred = None      # 父顶点
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self, neighborId, weight = 0):
        self.connectedTo[neighborId] = weight
    
    def setColor(self,color):
        self.color = color
    
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p
    
    def setDiscovery(self,dtime):
        self.disc = dtime
    
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
    

    def getColor(self):
        return self.color

    def getConnections(self):
        return self.connectedTo.keys()
    
    def getWeight(self, neighborId):
        return self.connectedTo[neighborId]
    
    def getId(self):
        return self.id
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
