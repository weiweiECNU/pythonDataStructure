class DoubleNode:
    """每个节点对象必须持有至少两条信息。首先，节点必须包含列 表元素本身。
    我们将这称为该节点的“数据区”(data field)。
    在此实现中，每个 节点都有对下一个节点的引用(通常称为“后继”next)和对前一个节点的引用(通常称为“前驱” back)。
    节点类还包括访问和修改的常用方法:返回节点 数据和引用到下一项。"""

    def __init__(self,data):
        self.data = data
        self.next = None # 节点初始 接地
        self.back = None 
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def getBack(self):
        return self.back
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNode):
        self.next = newNode

    def setBack(self,newNode):
        self.back = newNode


